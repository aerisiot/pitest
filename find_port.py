#!/usr/bin/env python
import time
import serial
import serial.tools.list_ports

gammurc = open('.gammurc', 'w+')

ports = list(serial.tools.list_ports.grep('USB'))
ports.sort()

for p in ports:
    device = p.device
    ser = serial.Serial(
        port=device,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    time.sleep(2)
    out = ''
    ser.write('ATI\r\n')
    time.sleep(1)
    while ser.inWaiting() > 0:
        out += ser.read(1)
    if out == '':
        print(device + ': no response')
    else:
        print(device + '\n' + out)
        if out.find('IMEI') != -1:
            gammurc.write('[gammu]\n')
            gammurc.write('port = ' + device + '\n')
            gammurc.write('connection = at115200\n')

