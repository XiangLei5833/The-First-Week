#!/usr/bin/env python3

def fib(n):
    current = 0        
    a,b = 1,1
    while current < n:
        yield a
        a,b = b, a+b
        current += 1    
