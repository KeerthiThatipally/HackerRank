#!/bin/python3

import sys

N=int(input().strip())
strs=[]
for i in range(N):
    str=input()
    strs.append(str)


for i in strs:
    str_temp = ''
    str_temp1 = ''
    for j in range(i.__len__()):

        if(j%2==0):
            str_temp=str_temp+i[j]
        else:
            str_temp1=str_temp1+i[j]
    print(str_temp+" "+str_temp1)