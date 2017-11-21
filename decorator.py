#!/usr/bin/env python3

from datetime import datetime

def log(func):
    def decorator(*args, **kwargs):
        print('Function ' + func.__name__ + 'has been called at' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return decorator

@log
def add(x, y):    # 相当于log(add),即调用了log函数，将add函数作为参数传递给log
    return x+y    # log先执行自带的函数decorator，打印出来信息，然后回调传入的func，即add

add.__name__    # 装饰器带来的副作用，add已经不是add了，他变成了log函数返回的decorator


