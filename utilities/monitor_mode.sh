#!/bin/bash

if [ $# -ne 1 ]
  then
    echo "Please input Wi-Fi adapter interface as input parameter!"
    exit
fi

wi-fi_interface=$1

sudo ifconfig wi-fi_interface down
sudo iwconfig wi-fi_interface mode monitor
sudo ifconfig wi-fi_interface up