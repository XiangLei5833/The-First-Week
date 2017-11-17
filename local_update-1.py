#!/usr/bin/env python3

def change():
    global a 
    a = 90
    print(a)

a = 9
print('Before', a)
print('Inside', end=' ')
change()
print('After', a)
