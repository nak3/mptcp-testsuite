#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   virt-construct.py: Automation tool for virt-install and kickstart
#
#   2012/08/22 ver1.0
#   2012/08/29 ver1.1
#       Environmental variable replacement rule is added.
#       Options -d and -s are added.
#   2012/09/15  ver1.2
#       Generic escape character for ks.conf ( '\x' -> 'x' )
#       License changed to GPLv2+
#
# Copyright (C) 2012 Etsuji Nakai
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, sys, re, tempfile, stat, time, argparse
import libvirt

class Config():
    def __init__( self ):
        # Instance variables
        self.virtInstallOpts = ""
        self.ksContentsList = []

    def parse( self, configFile ):
        configList = configFile.readlines()
        variableDict = self.__parseVariables( configList )
        self.virtInstallOpts = self.__parseVirtInstOpts(
                                            configList, variableDict )
        self.ksContentsList = self.__parseKickstart(
                                            configList, variableDict )

    def __replaceVariables( self, source, variableDict ):
        for variable in variableDict:
            source = source.replace(
                    '${' + variable + '}', variableDict[ variable ] )
        return source

    def __parseKickstart( self, configList, variableDict ):
        _ksContentsList = []
        sectionRe = re.compile( '^\[\S*\]' )
        kickstartSectionRe = re.compile( '^\[kickstart\]' )
        pos = 'pre'
        for line in configList:
            line = line.strip()   # We don't cut comment
            if pos == 'pre':
                if kickstartSectionRe.match( line ): pos = 'in'
                continue
            if pos == 'in':
                if sectionRe.match( line ): break # next section
                line = self.__replaceVariables( line, variableDict )
                line = re.sub( r'\\(.)', r'\1', line )  # Escaped charcter
                _ksContentsList.append( line + '\n' )
                continue
        return _ksContentsList

    def __parseVirtInstOpts( self, configList, variableDict ):
        _virtInstallOpts = ""
        sectionRe = re.compile( '^\[\S*\]' )
        vartInstSectionRe = re.compile( '^\[virt-install\]' )
        pos = 'pre'
        for line in configList:
            line = line.strip().split( '#' )[0]   # Cut comment
            if pos == 'pre':
                if vartInstSectionRe.match( line ): pos = 'in'
                continue
            if pos == 'in':
                if sectionRe.match( line ): break # next section
                _virtInstallOpts = ' '.join( ( _virtInstallOpts, line ) )
                continue
        return self.__replaceVariables( _virtInstallOpts, variableDict )

    def __parseVariables( self, configList ):
        _variableDict = {}
        sectionRe = re.compile( '^\[\S*\]' )
        variablesSectionRe = re.compile( '^\[variables\]' )
        nameAndVariableRe = re.compile( '^(\S+)\s*=\s*(\S+)\s*$' )
        envValReplaceRe = re.compile( '_(\S+)_' )
        pos = 'pre'
        for line in configList:
            line = line.strip().split( '#' )[0]   # Cut comment

            if pos == 'pre':
                if variablesSectionRe.match( line ): pos = 'in'
                continue

            if pos == 'in':
                if sectionRe.match( line ): break # next section
                pair = nameAndVariableRe.search( line )
                if pair:
                    variable, value = pair.group( 1 ), pair.group( 2 )
                    if variable.endswith( '_' ):
                        variable = variable.rstrip( '_' )
                        for envVal in envValReplaceRe.finditer( value ):
                            value = value.replace( envVal.group( 0 ),
                                os.environ.get( envVal.group( 1 ) ) or '' )
                    _variableDict[ variable ] = value
                continue

        return _variableDict


def parseArgs():
    parser = argparse.ArgumentParser(
        description='Build KVM virtual machine' )
    parser.add_argument( '-c', '--conf', type=argparse.FileType('r'),
        default=sys.stdin, help='Config file' )
    parser.add_argument( '-d', '--ksDir',
        default='/var/www/html/ks', help='directory to place ks.cfg' )
    parser.add_argument( '-b', '--ksBaseurl',
        default='http://192.168.122.1/ks', help='baseurl for ks.cfg' )
    parser.add_argument( '-s', '--startvm', action='store_true',
        default=False, help='start vm after installed' )
    parser.add_argument( '-n', '--dryrun', action='store_true',
        default=False, help='dryrun' )
    args = parser.parse_args()
    return args


def parseOpts():
    args = parseArgs()
    ksBaseurl = args.ksBaseurl.rstrip( '/' )
    ksDir = args.ksDir.rstrip( '/' )
    config = Config()
    config.parse( args.conf )
    return ( ksBaseurl, ksDir, config.virtInstallOpts, config.ksContentsList,
            args )


def checkVmStatus( vmName, status ):
    conn = libvirt.open( 'qemu:///system' )
    if status == 'running':
        runningVms = map( conn.lookupByID, conn.listDomainsID() )
        if vmName in [ vm.name() for vm in runningVms ]:
            return True
        else:
            return False

    if status == 'stopped':
        stoppedVms = conn.listDefinedDomains()
        if vmName in stoppedVms:
            return True
        else:
            return False


def waitVmStatus( vmName, status, timeoutSec ):
    count = timeoutSec
    while count > 0:
        print "Waiting %s to become %s (%d/%d)..." % (
                vmName, status, count, timeoutSec )
        if checkVmStatus( vmName, status ):
            print "Done."
            return True
        time.sleep( 10 )
        count -= 10
    return False

def startVm( vmName ):
    conn = libvirt.open( 'qemu:///system' )
    try:
        vm = conn.lookupByName( vmName )
        vm.create()
    except ( RuntimeError ):
        return False
    return True


if __name__ == '__main__':
    __debug = 1

    ( ksBaseurl, ksDir, virtInstallOpts, ksContentsList, args ) = parseOpts()

    # create ks.cfg and start virt-install
    with tempfile.NamedTemporaryFile( dir=ksDir, mode='w+t' ) as ksFile:
        ksFile.writelines( ksContentsList )
        ksFile.flush()
        os.chmod( ksFile.name, 0644 )
        ksFile_url = ksFile.name.replace( ksDir, ksBaseurl )
        virtInstallCmd = ' '.join(
                    ( 'virt-install', virtInstallOpts,
                      '--noautoconsole', '--noreboot',
                      '--extra-args="ks=' + ksFile_url + '"' ) )
        if __debug:
            print "== ks.cfg contents"
            os.system( 'cat ' + ksFile.name )
            print "== virt-install command"
            print virtInstallCmd
        if not args.dryrun:
            os.system( virtInstallCmd )

        vmNameRe = re.compile( '--name\s+(\S+)' )
        vmName = vmNameRe.search( virtInstallOpts ).group( 1 )
        if not waitVmStatus( vmName, 'running', timeoutSec=60 ):
            sys.exit( "Timeout to start installing vm %s." % vmName )
        if not waitVmStatus( vmName, 'stopped', timeoutSec=3600 ):
            sys.exit( "Timeout to finish installing vm %s." % vmName )
        if args.startvm:
            if not startVm( vmName ):
                sys.exit( "Failed to start vm %s." % vmName )
