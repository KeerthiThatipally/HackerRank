#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

d={}


for i in c:
    if d.__contains__(i):
        temp=d.__getitem__(i)
        temp=temp+1
        d.__setitem__(i,temp)
    else:
        d.__setitem__(i,1)

count = 0
for i in d.keys():

    temp=int(d.__getitem__(i)/2)

    if (temp>0):
        count=count+temp

print(count)



