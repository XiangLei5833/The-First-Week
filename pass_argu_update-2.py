#!/usr/bin/env python3

''' 可变长度的参数 '''

def connect(ipaddress, *ports):
    print('IP: ',ipaddress)
    for port in ports:
        print("port: ",port)

connect('192.168.1.1', 22, 35, 89)
