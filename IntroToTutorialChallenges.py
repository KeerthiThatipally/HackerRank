#!/bin/python3

import sys



V=int(input().strip())
n=int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(n):
    if(arr[i]==V):
        print(i)
