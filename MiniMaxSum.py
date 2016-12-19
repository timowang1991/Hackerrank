#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
arr = sorted([int(a),int(b),int(c),int(d),int(e)])

print sum(arr[:4])
print sum(arr[-4:])