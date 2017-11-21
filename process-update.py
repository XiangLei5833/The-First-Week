#!/usr/bin/env python3

import time
from multiprocessing import Process, Value

def func(val):
    for i in range(50):
        time.sleep(0.01)
        val.value += 1

if __name__ == '__main__':
    v = Value('i', 0)    # 多进程无法使用全局变量，Value()函数可以代理使共享
    procs = [Process(target=func, args=(v,)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()

    print(v.value)    

# 多进程推进顺序无法预测，多核就会同时进行多个进程，而不是一个接一个，而只有最后一个进程的结果会保留，这就导致结果可能不为500

