#!/usr/bin/env python3

from multiprocessing import Pool

def f(i):
    print(i, end=' ')

def main():
    pool = Pool(processes = 3)    # 初始化进程池
    for i in range(30):
        pool.apply(f, (i,))    # 输入第二个参数为元组，apply()传入不定参数


if __name__ == '__main__':
    main()
