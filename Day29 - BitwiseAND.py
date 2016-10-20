#!/bin/python3

import sys

max=0
t = int(input().strip())
and_var=0
for a0 in range(t):
    max=0
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    i=1
    for i in range(1,n+1):
        print("i is:",i)
        for j in range(i+1,n+1):
            and_var=i&(j)

            if(and_var>max and and_var<k):
                max=and_var
    print(max)

