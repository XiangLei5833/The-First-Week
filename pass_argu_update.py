#!/usr/bin/env python3

'''仅允许使用参数名传递参数'''
def hello(*, name = 'User'):
    print ("Hello", name)

hello(name = 'shiyanlou')
