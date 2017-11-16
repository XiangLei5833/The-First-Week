#!/usr/bin/env python

filename = '/etc/protocols'
f = open(filename)
try:
    f.write('shiyanlou')
except:
    print('File write error')
finally:
    print('Finally')
    f.close()
