#!/bin/python3

import sys


n=int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

i=n-2
temp=arr[n-1]
isStart=0

while(i>=0):

    if(temp<arr[i]):
        arr[i+1]=arr[i]
        print(str(arr).strip('[]').replace(',',''))
        i=i-1
    else:
        isStart=1
        arr[i+1]=temp
        print(str(arr).strip('[]').strip(',').replace(',',''))
        break


if(isStart==0):
    arr[0]=temp
    print(str(arr).strip('[]').strip(',').replace(',',''))


