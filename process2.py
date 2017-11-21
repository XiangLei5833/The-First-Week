#!/usr/bin/env python3

import time
from multiprocessing import Process, Value, Lock

def func(val):
    for i in range(50):
        time.sleep(0.01)    # 推迟调用线程的运行，挂起一段时间
        with lock:
            val.value += 1　　# lock.acquire()  val.value += 1  lock.release()


if __name__ == '__main__':
    v = Value('i', 0)    # 初始化为0
    lock = Lock()
    procs = [Process(target=func, args=(v, lock)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(v.value)

#　为什么不放到一个for循环，因为多个进程，需要start()...,join()....的格式
    
        
