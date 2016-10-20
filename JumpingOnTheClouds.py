#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

i=0
mov=0
while(i<n):
    if(c[i+2]==0):
        i=i+2
        mov=mov+1
    elif(c[i+1]==0):
        i=i+1
        mov=mov+1

print(mov)



