#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
lis=[]
temp=[]
min1=0

