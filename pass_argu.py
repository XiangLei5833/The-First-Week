#!/usr/bin/env python3

def connect(ipaddress, port):
    print('IP: ', ipaddress)
    print('port: ', port)

connect('192.168.1.1', 22)
connect(22, '192.168.1.1')
connect(port = 22, ipaddress = '192.168.1.1')
