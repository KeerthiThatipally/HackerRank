#!/bin/python3

import sys


n = int(input().strip())
for a0 in range(n):

    s = input().strip()
    list=[0]*26
    for i in range(s.__len__()):
        t=ord(s[i])-ord('a')
        list[t]=list[t]+1

    count=0
    for i in list:
        if(i>0):
            count=count+1


    print(count)


