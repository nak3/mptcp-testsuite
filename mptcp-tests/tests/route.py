#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser

from lib.utils import do_ssh,do_ssh_back


def network_ping_test():
    print ""
    print "    === network_ping_test ==="
    print ""

    do_ssh(client_eth0, ssh_port, "ping -c 1 " +server_eth1)
    do_ssh(client_eth0, ssh_port, "ping -c 1 " +server_eth2)

    do_ssh(server_eth0, ssh_port, "ping -c 1 " +client_eth1)
    do_ssh(server_eth0, ssh_port, "ping -c 1 " +client_eth2)


def network_traceroute_test():
    print ""
    print "    === network_traceroute_test ==="
    print ""

    do_ssh(client_eth0, ssh_port, "traceroute " +server_eth1)
    do_ssh(client_eth0, ssh_port, "traceroute " +server_eth2)

    do_ssh(server_eth0, ssh_port, "traceroute " +client_eth1)
    do_ssh(server_eth0, ssh_port, "traceroute " +client_eth2)


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

    network_ping_test()
    network_traceroute_test()
