#!/bin/python3

import sys


n = int(input().strip())




count=0
for i in range(n):
    if((n+i)==(bin(n)^bin(i))):
        count=count+1
print(count)