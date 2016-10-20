#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(arr)
sum=0
for i in arr:
    sum = sum + i
print(sum)