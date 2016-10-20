#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    count=0
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    if(n>=k):
        for i in a:
            if(i<0 or i==0):
                count=count+1

        if (count < k):
            print("YES")
        else:
            print("NO")


