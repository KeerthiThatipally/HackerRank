#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
j=n-1
sum_1=0
sum_2=0
for i in range(n):
    sum_1=sum_1+a[i][i]
    sum_2=sum_2+a[i][j]
    j=j-1
print(abs(sum_1-sum_2))