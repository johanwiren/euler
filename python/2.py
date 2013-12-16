#!/usr/bin/env python

def fib(max):
    i, j = 1, 2
    while j <= max:
        yield i
        i, j = j, i + j
        
print sum([ x for x in fib(4000000) if not x % 2 ])
