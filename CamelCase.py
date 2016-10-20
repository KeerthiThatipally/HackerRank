#!/bin/python3

import sys


s = input().strip()
print(s)

if(s.__len__()>0):
    count = 1
    for i in s:
        if(65<=ord(i)<=90):
            count=count+1
    print(count)