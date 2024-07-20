#!/bin/bash

if [ $# -ne 1 ]
  then
    echo "Please input Wi-Fi adapter interface as input parameter!"
    exit
fi

wifi_interface=$1

sudo ifconfig $wifi_interface down
sudo iwconfig $wifi_interface mode monitor
sudo ifconfig $wifi_interface up
