#!/usr/bin/env python3

class Animal(object):
    owner = 'jack'    # 此为静态变量，可以通过类名直接访问。
   
    def __init__(self, name):
        self._name = name

    @classmethod
    def get_owner(cls):    # 类方法需要类作为第一个参数，它是由解释器传给方法
        return cls.owner
