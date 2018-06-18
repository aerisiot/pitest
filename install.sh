#!/bin/bash
sudo apt-get install -y usb-modeswitch gammu ppp wvdial tcpdump
sudo apt-get purge --auto-remove -y wolfram-engine
sudo apt-get clean
echo Copying config files ...
sudo cp wvdial.conf /etc/wvdial.conf
sudo cp .gammurc ~/.gammurc
pip install requests configparser
bash setup.sh

