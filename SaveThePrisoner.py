#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,m,s=input().strip().split(" ")
    n=int(n)
    m=int(m)
    s=int(s)
    res=(s+m-1)%n
    if(res==0):
        print(n)
    else:
        print(res)
