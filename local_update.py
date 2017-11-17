#!/usr/bin/env python3

a = 9

def change():
    global a
    print(a)

print("Before", a)
print("Inside", end = ' ')
change()
print("After", a)


