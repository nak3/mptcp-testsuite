#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def do_ssh(host,port,cmd):
        return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+ port +" root@"+ host +" \""+ cmd +"\"")

def do_ssh_back(host, port, cmd):
        return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@" +host+ " "+cmd)

def set_path_manager(host, port, path_manager):
	do_ssh(host, port, "sysctl -w net.mptcp.mptcp_path_manager='" + path_manager +"'")
