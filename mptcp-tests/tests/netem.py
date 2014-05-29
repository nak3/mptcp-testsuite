#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import time
from lib.utils import do_ssh,do_ssh_back

def tcpdump_route1_test():
    print ""
    print "    === tcpdump_route1_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth1) -- router(eth1) -- router(eth3) --> server(eth1)    |"
    print " |   set up tcpdump (or tshark) on router(eth1) and router(eth1)      |"
    print " --------------------------------------------------------------------- "
    print ""

    # do_ssh_back(router_eth0, ssh_port, "tcpdump  -w /var/tmp/network_tcpdump_route1_test.dump -i eth2 -i eth1  2>&1 &")
    do_ssh_back(router_eth0, ssh_port, "tshark -s 150 -i eth1 -i eth2 -n -w /var/tmp/network_tcpdump_route1_test.dump tcp 2>&1 &")

    do_ssh(client_eth0, ssh_port, "tc qdisc add dev "+ client_eth1 +" root netem delay 500ms > /dev/null 2>&1")
    do_ssh(client_eth0, ssh_port, "tc qdisc show dev "+ client_eth1)
    time.sleep(5)

    do_ssh(client_eth0, ssh_port, "curl " +server_eth1+ " > /dev/null 2>&1")

    time.sleep(10)

    # do_ssh(router_eth0, ssh_port, "tshark -r /var/tmp/network_tcpdump_route1_test.dump")
    do_ssh(router_eth0, ssh_port, "tcpdump -r /var/tmp/network_tcpdump_route1_test.dump")
    do_ssh(router_eth0, ssh_port, "pkill tshark ; pkill tcpdump")
    do_ssh(router_eth0, ssh_port, "rm -f /var/tmp/network_tcpdump_route1_test.dump")

    return


def tcpdump_route2_test():

    print ""
    print "    === tcpdump_route2_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth2) -- router(eth2) -- router(eth4) --> server(eth2)    |"
    print " |   set up tcpdump (or tshark) on router(eth1) and router(eth2)      |"
    print " --------------------------------------------------------------------- "
    print ""


    # do_ssh_back(router_eth0, ssh_port, "tcpdump  -w /var/tmp/network_tcpdump_route2_test.dump -i eth2 -i eth1  2>&1 &")
    do_ssh_back(router_eth0, ssh_port, "tshark -s 150 -i eth1 -i eth2 -n -w /var/tmp/network_tcpdump_route2_test.dump tcp 2>&1 &")

    time.sleep(5)

    do_ssh(client_eth0, ssh_port, "curl " +server_eth2+ " > /dev/null 2>&1")

    time.sleep(10)

    # do_ssh(router_eth0, ssh_port, "tshark -r /var/tmp/network_tcpdump_route2_test.dump")
    do_ssh(router_eth0, ssh_port, "tcpdump -r /var/tmp/network_tcpdump_route2_test.dump")
    do_ssh(router_eth0, ssh_port, "pkill tshark ; pkill tcpdump")
    do_ssh(router_eth0, ssh_port, "rm -f /var/tmp/network_tcpdump_route2_test.dump")

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

    tcpdump_route1_test()
    tcpdump_route2_test()
