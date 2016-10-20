#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
difflist=[]

min=100**100
diff=0
for i in range(n):
    for j in range(i+1,n):
        if(A[i]==A[j]):
            diff=abs(i-j)
            if(diff<min):
                min=diff

if not (diff==0):
    print(min)
else:
    print("-1")