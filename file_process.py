#!/usr/bin/env python3

file = open('/etc/protocols')
type(file)
print(file)
file.close

with open('/etc/protocols') as file:    # try-finally 的简写，无须考虑关闭
    count = 0
    for line in file:
        count += 1
    print(count)
