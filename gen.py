from __future__ import generators

def evens(n):
    i = 0
    while 2*i <= n:
        yield 2*i
        i += 1

	
