#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser
import time
from lib.utils import do_ssh,do_ssh_back


def bigdata_route1_test():
    print ""
    print "    === bigdata_route1_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth1) -- router(eth1) -- router(eth3) --> server(eth1)    |"
    print " |   wget BIGDATA FILE from server to client                          |"
    print " --------------------------------------------------------------------- "
    print ""

    # do_ssh_back(router_eth0, ssh_port, "tcpdump  -w /var/tmp/network_tcpdump_route1_test.dump -i eth2 -i eth1  2>&1 &")
    do_ssh_back(router_eth0, ssh_port, "tshark -s 150 -i eth1 -i eth2 -n -w /var/tmp/network_tcpdump_route1_test.dump tcp 2>&1 &")

    time.sleep(5)

    do_ssh(server_eth0, ssh_port, "mkdir -p /var/www/html/bigdata")
    do_ssh(server_eth0, ssh_port, "dd if=/dev/zero of=/var/www/html/bigdata/1M bs=1M count=1")

    do_ssh(client_eth0, ssh_port, "mkdir -p /root/bigdata/")
    do_ssh(client_eth0, ssh_port, "wget -P /root/bigdata " +server_eth1+ "/bigdata/1M  > /dev/null 2>&1")

    time.sleep(10)

    # do_ssh(router_eth0, ssh_port, "tshark -r /var/tmp/network_tcpdump_route1_test.dump")
    do_ssh(router_eth0, ssh_port, "tcpdump -r /var/tmp/network_tcpdump_route1_test.dump")

    do_ssh(router_eth0, ssh_port, "pkill tshark ; pkill tcpdump")
    do_ssh(router_eth0, ssh_port, "rm -f /var/tmp/network_tcpdump_route1_test.dump")

    do_ssh(client_eth0, ssh_port, "rm -f /root/bigdata/")
    do_ssh(server_eth0, ssh_port, "rm -rf /var/www/html/bigdata")

    return


def bigdata_route2_test():
    print ""
    print "    === bigdata_route2_test ==="
    print ""
    print " --------------------------------------------------------------------- "
    print " |   client(eth2) -- router(eth2) -- router(eth4) --> server(eth2)    |"
    print " |   wget BIGDATA FILE from server to client                          |"
    print " --------------------------------------------------------------------- "
    print ""

    # do_ssh_back(router_eth0, ssh_port, "tcpdump  -w /var/tmp/network_tcpdump_route1_test.dump -i eth2 -i eth1  2>&1 &")
    do_ssh_back(router_eth0, ssh_port, "tshark -s 150 -i eth1 -i eth2 -n -w /var/tmp/network_tcpdump_route1_test.dump tcp 2>&1 &")

    time.sleep(5)

    do_ssh(server_eth0, ssh_port, "mkdir -p /var/www/html/bigdata")
    do_ssh(server_eth0, ssh_port, "dd if=/dev/zero of=/var/www/html/bigdata/1M bs=1M count=1")

    do_ssh(client_eth0, ssh_port, "mkdir -p /root/bigdata/")
    do_ssh(client_eth0, ssh_port, "wget -P /root/bigdata " +server_eth2+ "/bigdata/1M  > /dev/null 2>&1")

    time.sleep(10)

    # do_ssh(router_eth0, ssh_port, "tshark -r /var/tmp/network_tcpdump_route1_test.dump")
    do_ssh(router_eth0, ssh_port, "tcpdump -r /var/tmp/network_tcpdump_route1_test.dump")

    do_ssh(router_eth0, ssh_port, "pkill tshark ; pkill tcpdump")
    do_ssh(router_eth0, ssh_port, "rm -f /var/tmp/network_tcpdump_route1_test.dump")

    do_ssh(client_eth0, ssh_port, "rm -f /root/bigdata/")
    do_ssh(server_eth0, ssh_port, "rm -rf /var/www/html/bigdata")


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

    bigdata_route1_test()
    bigdata_route2_test()
