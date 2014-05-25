mptcp-testsuite
===============

Tests of mptcp-kernel for Linux environment. The mptcp-testsuite creates simple environment and tests. It allows to create KVM environment with three mptcp-kernel guests by default.


Usage
--------

Step0. clone this repository

`git clone https://github.com/nak3/mptcp-testsuite.git`

Step1. create virtual machines  (You needs to start apache httpd service and install virt-install)

`sudo mkdir /var/www/html/ks`

`cd mptcp-testsuite/kvm-setup`

`sudo python virt-construct.py -c conf/mptcp-client.conf`

`sudo python virt-construct.py -c conf/mptcp-router.conf`

`sudo python virt-construct.py -c conf/mptcp-server.conf`

`sudo virsh start mptcp-client ; sudo virsh start mptcp-router ; sudo virsh start mptcp-server`

Step2. Initial configuration

`cd ../mptcp-tests`

`python initial-setup.py`

__MEMO: password is "mptcp"__

Step3. Now, you can exec tests.

eg. test your network configutation

`python exec.py route`

eg. check the mptcp packet

`python exec.py tcpdump`

_MEMO: This setups create new three virtual machines and network configuration. See more [details](https://github.com/nak3/mptcp-testsuite/blob/master/kvm-setup/README.md)_.


Test list
---------

You can test by `python exec.py ${TestName}` or if you would like to test all, `python exec.py all`

__NOTE: This is still work in progress__

| TestName   | Summary                                            |
|:-----------|:---------------------------------------------------|
| route      | ping and traceroute test between client and server |
| tcpdump    | exec tcpdump test between client and server        |
| iperf      | simple iperf test between client and server        |
| qperf      | simple qperf test between client and server        |


Contact
---------

If you have any question, comment or request, please tell me by following E-mail address in English or Japanese.

Mail To: nakayamakenjiro at gmail dot com (Kenjiro Nakayama)
