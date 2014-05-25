#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import time
from lib.utils import do_ssh,do_ssh_back

def qperf_tcp_lat_route1_test():
    print ""
    print "    === qperf_tcp_lat_route1_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth1) -- router(eth1) -- router(eth3) --> server(eth1)    |"
    print " |   set up qperf on client and server                                |"
    print " --------------------------------------------------------------------- "
    print ""

    do_ssh_back(server_eth0, ssh_port, "qperf &")

    time.sleep(3)

    do_ssh(client_eth0, ssh_port, "qperf -v " + server_eth1 + " tcp_lat")

    do_ssh(server_eth0, ssh_port, "pkill qperf")

    return


def qperf_tcp_lat_route2_test():
    print ""
    print "    === qperf_tcp_lat_route1_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth2) -- router(eth2) -- router(eth4) --> server(eth2)    |"
    print " |   set up qperf on client and server                                |"
    print " --------------------------------------------------------------------- "
    print ""

    do_ssh_back(server_eth0, ssh_port, "qperf &")

    time.sleep(3)

    do_ssh(client_eth0, ssh_port, "qperf -v " + server_eth2 + " tcp_lat")

    do_ssh(server_eth0, ssh_port, "pkill qperf")

    return


if __name__ == '__main__':

    config = ConfigParser.SafeConfigParser()
    config.read('network.conf')

    client_eth0 = config.get("client","client_eth0")
    router_eth0 = config.get("router","router_eth0")
    server_eth0 = config.get("server","server_eth0")

    client_eth1 = config.get("client","client_eth1")
    router_eth1 = config.get("router","router_eth1")
    server_eth1 = config.get("server","server_eth1")

    client_eth2 = config.get("client","client_eth2")
    router_eth2 = config.get("router","router_eth2")
    server_eth2 = config.get("server","server_eth2")

    client_eth3 = config.get("client","client_eth3")
    router_eth3 = config.get("router","router_eth3")
    server_eth3 = config.get("server","server_eth3")

    client_eth4 = config.get("client","client_eth4")
    router_eth4 = config.get("router","router_eth4")
    server_eth4 = config.get("server","server_eth4")

    ssh_port = config.get("port","ssh_port")

    qperf_tcp_lat_route1_test()
    qperf_tcp_lat_route2_test()
