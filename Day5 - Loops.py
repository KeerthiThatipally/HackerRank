#!/bin/python3

import sys


N = int(input().strip())

for i in range(1,11):
    res=N*i
    print(str(N)+" x "+str(i)+" = "+str(res))