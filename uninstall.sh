#!/bin/bash
pip uninstall -q -y pyserial requests configparser
sudo rm -rf "$NVM_DIR"
sudo apt-get purge --auto-remove -q -y tcpdump wvdial ppp gammu usb-modeswitch
sudo apt-get clean

