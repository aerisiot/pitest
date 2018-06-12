#!/usr/bin/env python

import time

import serial.tools.list_ports

print("Available ports: \r\n")
pcount = 0
ports = list(serial.tools.list_ports.comports())
ports.sort()
for p in ports:
    print(str(pcount) + ":" + str(p))
    pcount = pcount + 1

portnum = int(raw_input("\r\nChoose the port number: "))
myport = str(ports.pop(portnum)).split(' ', 1).pop(0)
print("Using port: " + myport + "\r\n")

ser = serial.Serial(

    port=myport,
    # port='/dev/ttyUSB3',
    baudrate = 9600,
    # baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


def sendATcmd(atcmd):
    out = ''
    ser.write(atcmd + '\r\n')
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out != '':
        print
        ">>" + out


# Some time to open
time.sleep(2)

print("I: Identification command")
sendATcmd('ATI')

print("CIMI: Return IMSI")
sendATcmd('AT+CIMI')

print("CSQ: Signal quality")
sendATcmd('AT+CSQ')

print("CREG: Network registration report")
sendATcmd('AT+CREG?')

print("COPS: Operator selection")
sendATcmd('AT+COPS?')
