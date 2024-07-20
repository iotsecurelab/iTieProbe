#!/bin/bash

if [ $# -ne 4 ]
  then
    echo "Please input AP SSID, AP MAC, Channel, and Wi-Fi adapter interface as input parameter!"
    exit
fi

ap_ssid=$1
ap_mac=$2
channel=$3
wifi_interface=$4

sudo airbase-ng -e $ap_ssid -a $ap_mac -c $channel $wifi_interface
