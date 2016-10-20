#!/bin/python3

import sys

n= int(input().strip())

for i in range(n):
    count=0
    s = input().strip()
    for i in range(s.__len__()-1):
        if(s[i]==s[i+1]):
            count=count+1
    print(count)






