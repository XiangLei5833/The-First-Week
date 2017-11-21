#!/usr/bin/env python3

from multiprocessing import Process, Queue

queue = Queue(maxsize = 10)    # 可以在初始化时指定一个最大容量

def f1():
    queue.put('Hello shiyanlou')

def f2():
    data = queue.get()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()


if __name__ == '__main__':
    main()
