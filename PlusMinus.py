#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)
neg,pos,zero=0,0,0
for a in arr:
    if(a<0):
        neg=neg+1
    elif((a)>0):
        pos=pos+1
    else:
        zero=zero+1
print("%.6f" % (pos/n))
print("%.6f" % (neg/n))
print("%.6f" % (zero/n))

