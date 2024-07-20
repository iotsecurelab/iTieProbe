#!/bin/bash

if [ $# -ne 2 ]
  then
    echo "Please configure DHCP evil twin IP and netmask as input parameter!"
    exit
fi

evil_twin_ip=$1
netmask=$2

ifconfig at0
ifconfig at0 up
ifconfig at0 $evil_twin netmask $netmask
dhcpd -cf /etc/dhcp/dhcpd.conf
service isc-dhcp-server restart
