#!/bin/bash
pip uninstall -y requests configparser
sudo rm -rf "$NVM_DIR"
sudo apt-get purge --auto-remove -y tcpdump wvdial ppp gammu usb-modeswitch
sudo apt-get clean

