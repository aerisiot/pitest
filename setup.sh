#!/bin/bash
gammu identify > info.txt
device=$(grep "Device" info.txt)
dev="${device:23:12}"
echo "${dev}"

