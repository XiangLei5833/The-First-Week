#!/usr/bin/env python

class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self._name = name

    @staticmethod    # 静态方法即不需要实例也可以进行调用，放到外面可以是一个独立的方法
    def order_animal_food():
        print('ording...')
        print('ok')
