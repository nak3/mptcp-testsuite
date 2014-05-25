#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser

from tests.lib.utils import do_ssh

def debug_setup():
    do_ssh(client_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_debug=1")
    do_ssh(router_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_debug=1")
    do_ssh(server_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_debug=1")


def network_default_setup():
    #client
    do_ssh(client_eth0, ssh_port, "ip rule add from 10.1.1.1 table 1")
    do_ssh(client_eth0, ssh_port, "ip route add 10.1.1.0/24 dev eth1 scope link table 1")
    do_ssh(client_eth0, ssh_port, "ip route add 10.2.1.0/24 via 10.1.1.2")
    do_ssh(client_eth0, ssh_port, "ip route add default via 10.1.1.2 dev eth1 table 1")

    do_ssh(client_eth0, ssh_port, "ip rule add from 10.1.2.1 table 2")
    do_ssh(client_eth0, ssh_port, "ip route add 10.1.2.0/24 dev eth2 scope link table 2")
    do_ssh(client_eth0, ssh_port, "ip route add 10.2.2.0/24 via 10.1.2.2")
    do_ssh(client_eth0, ssh_port, "ip route add default via 10.1.2.2 dev eth2 table 2")

    # router
    do_ssh(router_eth0, ssh_port, "sysctl net.ipv4.ip_forward=1")

    # router as a NAT
    # do_ssh(router_eth0, ssh_port, "iptables -t nat -A POSTROUTING -s 10.1.1.0/24 -j MASQUERADE")
    # do_ssh(router_eth0, ssh_port, "iptables -t nat -A POSTROUTING -s 10.1.2.0/24 -j MASQUERADE")
    #
    # do_ssh(router_eth0, ssh_port, "iptables -t nat -A POSTROUTING -s 10.2.1.0/24 -j MASQUERADE")
    # do_ssh(router_eth0, ssh_port, "iptables -t nat -A POSTROUTING -s 10.2.2.0/24 -j MASQUERADE")

    # server
    do_ssh(server_eth0, ssh_port, "ip rule add from 10.2.1.1 table 1")
    do_ssh(server_eth0, ssh_port, "ip route add 10.2.1.0/24 dev eth1 scope link table 1")
    do_ssh(server_eth0, ssh_port, "ip route add 10.1.1.0/24 via 10.2.1.2")
    do_ssh(server_eth0, ssh_port, "ip route add default via 10.2.1.2 dev eth1 table 1")

    do_ssh(server_eth0, ssh_port, "ip rule add from 10.2.2.1 table 2")
    do_ssh(server_eth0, ssh_port, "ip route add 10.2.2.0/24 dev eth2 scope link table 2")
    do_ssh(server_eth0, ssh_port, "ip route add 10.1.2.0/24 via 10.2.2.2")
    do_ssh(server_eth0, ssh_port, "ip route add default via 10.2.2.2 dev eth2 table 2")


def setup_nopass():
    #        os.system("ssh-keygen -N \"\"")
    os.system("ssh-copy-id root@" + client_eth0)
    os.system("ssh-copy-id root@" + router_eth0)
    os.system("ssh-copy-id root@" + server_eth0)


def setup_path_manager(manager_type):
    do_ssh(client_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_path_manager="+ manager_type)
    do_ssh(router_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_path_manager="+ manager_type)
    do_ssh(server_eth0, ssh_port, "sysctl -w net.mptcp.mptcp_path_manager="+ manager_type)


def setup_initial_service():
    do_ssh(client_eth0, ssh_port, "systemctl disable firewalld")
    do_ssh(client_eth0, ssh_port, "systemctl stop firewalld")
    do_ssh(client_eth0, ssh_port, "systemctl start iptables")
    do_ssh(client_eth0, ssh_port, "systemctl start httpd")

    do_ssh(router_eth0, ssh_port, "systemctl disable firewalld")
    do_ssh(router_eth0, ssh_port, "systemctl stop firewalld")
    do_ssh(router_eth0, ssh_port, "systemctl start iptables")
    do_ssh(router_eth0, ssh_port, "systemctl start httpd")

    do_ssh(server_eth0, ssh_port, "systemctl disable firewalld")
    do_ssh(server_eth0, ssh_port, "systemctl stop firewalld")
    do_ssh(server_eth0, ssh_port, "systemctl start iptables")
    do_ssh(server_eth0, ssh_port, "systemctl start httpd")


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

    setup_nopass()
    network_default_setup()
    debug_setup()
    setup_path_manager("fullmesh")
    setup_initial_service()
