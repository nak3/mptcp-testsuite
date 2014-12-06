#!/bin/bash


###
OLD_URL_F_MPTCP="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/fedora-20-x86_64/kernel-3.14.15-306.mptcp.fc20/kernel-3.14.15-306.mptcp.fc20.x86_64.rpm"
NEW_URL_F_MPTCP="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/fedora-20-x86_64/kernel-3.14.15-307.mptcp.fc20/kernel-3.14.15-307.mptcp.fc20.x86_64.rpm"

OLD_URL_F_MPTCP_P="/root/rpm/kernel-3.14.15-306.mptcp.fc20.x86_64.rpm"
NEW_URL_F_MPTCP_P="/root/rpm/kernel-3.14.15-307.mptcp.fc20.x86_64.rpm"

OLD_URL_F_MODULE="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/fedora-20-x86_64/kernel-3.14.15-306.mptcp.fc20/kernel-modules-extra-3.14.15-306.mptcp.fc20.x86_64.rpm"
NEW_URL_F_MODULE="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/fedora-20-x86_64/kernel-3.14.15-307.mptcp.fc20/kernel-modules-extra-3.14.15-307.mptcp.fc20.x86_64.rpm"

OLD_URL_F_MODULE_P="/root/rpm/kernel-modules-extra-3.14.15-306.mptcp.fc20.x86_64.rpm"
NEW_URL_F_MODULE_P="/root/rpm/kernel-modules-extra-3.14.15-307.mptcp.fc20.x86_64.rpm"


OLD_URL_C_MPTCP="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/epel-7-x86_64/kernel-3.14.15-306.mptcp.fc20/kernel-3.14.15-306.mptcp.el7.centos.x86_64.rpm"
NEW_URL_C_MPTCP="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/epel-7-x86_64/kernel-3.14.15-307.mptcp.fc20/kernel-3.14.15-307.mptcp.el7.centos.x86_64.rpm"

OLD_URL_C_MODULE="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/epel-7-x86_64/kernel-3.14.15-306.mptcp.fc20/kernel-modules-extra-3.14.15-306.mptcp.el7.centos.x86_64.rpm"
NEW_URL_C_MODULE="http://copr-be.cloud.fedoraproject.org/results/kenjiro/mptcp-kernel/epel-7-x86_64/kernel-3.14.15-307.mptcp.fc20/kernel-modules-extra-3.14.15-307.mptcp.el7.centos.x86_64.rpm"

OLD_URL_C_MPTCP_P="/root/rpm/kernel-3.14.15-306.mptcp.el7.centos.x86_64.rpm"
NEW_URL_C_MPTCP_P="/root/rpm/kernel-3.14.15-306.mptcp.el7.centos.x86_64.rpm"

OLD_URL_C_MODULE_P="/root/rpm/kernel-modules-extra-3.14.15-306.mptcp.el7.centos.x86_64.rpm"
NEW_URL_C_MODULE_P="/root/rpm/kernel-modules-extra-3.14.15-307.mptcp.el7.centos.x86_64.rpm"

sed -i s!$OLD_URL_F_MPTCP!$NEW_URL_F_MPTCP!g ./conf/*
sed -i s!$OLD_URL_F_MODULE!$NEW_URL_F_MODULE!g ./conf/*
sed -i s!$OLD_URL_F_MPTCP_P!$NEW_URL_F_MPTCP_P!g ./conf/*
sed -i s!$OLD_URL_F_MODULE_P!$NEW_URL_F_MODULE_P!g ./conf/*


sed -i s!$OLD_URL_C_MPTCP!$NEW_URL_C_MPTCP!g ./conf/*
sed -i s!$OLD_URL_C_MODULE!$NEW_URL_C_MODULE!g ./conf/*
sed -i s!$OLD_URL_C_MPTCP_P!$NEW_URL_C_MPTCP_P!g ./conf/*
sed -i s!$OLD_URL_C_MODULE_P!$NEW_URL_C_MODULE_P!g ./conf/*
