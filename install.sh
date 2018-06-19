#!/bin/bash
sudo apt-get install -y usb-modeswitch gammu ppp wvdial tcpdump
sudo apt-get purge --auto-remove -y wolfram-engine
sudo apt-get clean
pip install pyserial requests configparser
sudo chmod +x find_port.py
./find_port.py
echo Copying config files ...
sudo cp wvdial.conf /etc/wvdial.conf
sudo cp .gammurc ~/.gammurc

