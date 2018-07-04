#!/bin/bash
sudo ip route add 192.168.40.0/24 via 10.64.64.64 dev ppp0
netstat -rn
sudo tcpdump -nni ppp0 icmp

