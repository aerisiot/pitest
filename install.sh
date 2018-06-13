#!/bin/bash
sudo apt-get install -y usb-modeswitch gammu ppp wvdial tcpdump
sudo apt-get purge --auto-remove -y wolfram-engine
sudo apt-get clean
mkdir -p $HOME/.nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
nvm install node
echo Copying config files ...
sudo cp wvdial.conf /etc/wvdial.conf
sudo cp .gammurc ~/.gammurc