#!/bin/python3

import sys

n=int(input().strip())
arr=[int(arr_temp) for arr_temp in input().strip().split(' ')]
p=arr[0]

left=[]
right=[]
equals=[]

for i in range(n):
    if(arr[i]<p):
        left.append(arr[i])
    elif(arr[i]==p):
        equals.append(arr[i])
    else:
        right.append(arr[i])

res=str(left+equals+right)
print(res.strip('[]').replace(',',' '))

