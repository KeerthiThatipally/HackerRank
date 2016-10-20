#!/bin/python3

import sys

n=int(input().strip())
arr=[int(arr_temp) for arr_temp in input().strip().split(" ")]
i=1
temp=0
j=0
for i in range(1,n):
    j = i
    while(j>0):

        if(arr[j]<arr[j-1]):

            temp=arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp
        j=j-1
    print(str(arr).strip('[]').replace(',',''))





