kvm-setup for mptcp-testsuite
==========

kvm-setup allows you to create easily test environment for mptcp-kernel with three KVM guests.

Basic Usage
-----

`sudo python virt-construct.py -c conf/$CONFIGFILE`

eg)
`sudo python virt-construct.py -c conf/mptcp-client.conf`

virt-construct.py is forked from [enakai00's repository](https://github.com/nak3/mptcp-testsuite).


Default Network
-----
This is a default network configuration, which is the result of `python virt-construct.py -c conf/mptcp-*.conf`. IP address of each eth* will be set by mptcp-tests/initial-setup.py and mptcp-tests/network.conf.

![default network](https://github.com/nak3/mptcp-testsuite/blob/master/misc/pictures/default-network.png?raw=true)

Check default network [IP addresses](https://github.com/nak3/mptcp-testsuite/blob/master/mptcp-tests/network.conf)


Recommend
-----

You should change following URL which is the mirror repository to download Fedora 20 to use as guest. The default setting is using the site in Japan.

    # Please change url to your mirror site, this is in Japan.
    url=http://ftp.jaist.ac.jp/pub/Linux/Fedora/releases/20/Fedora/x86_64/os/

You can find your appropriate repository [here](https://mirrors.fedoraproject.org/publiclist/Fedora/20/x86_64/).


NOTE
-----

You may need to make directory.

`mkdir /var/www/html/ks`

Also, before using it, you may need to install some packages.
