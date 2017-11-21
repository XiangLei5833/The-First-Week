#!/usr/bin/env python3

import os
from multiprocessing import Process

def hello(name):
    print('child process: {}'.format(os.getpid()))
    print('Hello '+ name)

def main():
    p = Process(target=hello, args=('shiyanlou', ))    # target:指定进程执行的函数；args:该函数的参数（务必使用元组形式）
    p.start()    # start()表示启动进程
    p.join()     # join()为阻塞当前进程，知道调用join()的进程执行完了，才会执行当前进程，返回最后一句语句打印
    print('parent process: {}'.format(os.getpid()))


if __name__ == '__main__':
    main()

# Process() 的 run()方法，实例化Process的时候不指定target就会执行默认run方法，返回“run method”

# 调用多个进程的格式是：
# p1.start()
# p2.start()
# p1.join()
# p2.join()
