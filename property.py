#!/usr/bin/env python3

''' property 可以将方法变成一个属性使用，实现getter/setter '''

class Animal(object):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self, value):
        self._name = value
    
    def make_sound(self):
        pass
