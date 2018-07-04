#!/bin/bash
sudo apt-get install -q -y usb-modeswitch gammu ppp wvdial tcpdump
sudo apt-get purge --auto-remove -q -y wolfram-engine
pip install -q pyserial requests configparser
sudo chmod 755 find_port.py
./find_port.py
echo Copying config files ...
sudo cp wvdial.conf /etc/wvdial.conf
sudo cp .gammurc ~/.gammurc

