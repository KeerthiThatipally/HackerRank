#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
sticks=0

while(True):
    sticks = 0
    count=0
    small=arr[0]
    for i in range(n):
        if(arr[i]!=0):
            if(small==0):
                small=arr[i]
            if(arr[i]<small):
                small=arr[i]
        i+=1

    for i in range(n):
        if(arr[i]!=0):
            arr[i]=arr[i]-small

            count=0
            sticks=sticks+1
        else:
            count=count+1
        i=i+1

    if(count==n):
        break
    print(sticks)





