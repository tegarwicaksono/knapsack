# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:06:13 2016

@author: Tegar
"""

from collections import deque

from recordclass import recordclass

testTuple = recordclass('testTuple', 'name number rat')

seq = [testTuple('abc', 4, 2), testTuple('xyz', 32, 32), testTuple('def', 48, 12)]

a = testTuple('yay', 82, 41)
b = testTuple(None, None, None)
c = testTuple()

ite = []

print(a)

a.number = 164

print(a)

#a = testTuple(name = 'yay', number = 82, rat = 41)
#b = testTuple(name = None, number = None, rat = None )
q = deque([])

#q.append(a)
#if (q.empty):
#    print("it is empty")
print("size of q = ", len(q))
#print(q)

#print(seq)
#seq = sorted(seq, key=lambda testTuple : testTuple.number/testTuple.rat)
#print(seq)