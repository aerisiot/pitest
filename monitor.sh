#!/bin/bash

files=('SJ1-SJ-ASA-VPN.txt')

sendpings() {
    while IFS='' read -r line || [[ -n "$line" ]]; do
        ping -c 1 -I ppp0 "$line" > /dev/null
        if [ $? -eq 0 ]; then
            echo "$line is up"
        else
            echo "$line is down"
        fi
    done < "$1"
}

for i in "${files[@]}";do
    sendpings $i
done

