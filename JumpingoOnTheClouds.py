#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i=0
E=100
temp=c[0]
while(i<n):

    if(c[i]==0):

        E=E-1
    else:
        E=E-1-2
    i=i+k

print(E)
