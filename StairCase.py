#!/bin/python3

import sys


n = int(input().strip())

k = n - 1
for i in range(0,n):

    for j in range(0,n):
        if(j>=k):
            print('#', end="", flush=True)
        else:
            print(' ', end="", flush=True)
    k=k-1

    print()
