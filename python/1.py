#!/usr/bin/env python

def multiples_of_three_or_five():
    for i in range(1000):
        if ( i % 3 == 0 ) or ( i % 5 == 0 ):
            yield i
        
print sum([ x for x in multiples_of_three_or_five() ])

