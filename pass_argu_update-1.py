#!/usr/bin/env python

def f(a, data=[]):    # 默认参数为可变对象，函数的后续调用会持续累加
    data.append(a)
    return data

print(f(1))
print(f(2))
print(f(3))


def f(a, data1=None):    # 这个时候需要将可变对象设置为 None，即可避免
    if data1 is None:    # is 比等号更加的精确，是数值和地址的统一
        data1 = []
    data1.append(a)
    return data1

print(f(1))
print(f(2))
print(f(3))
