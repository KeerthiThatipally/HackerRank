#!/bin/python3

import sys


t = int(input().strip())




rem_val = 3
while t > rem_val:
    t = t-rem_val
    rem_val *= 2

print(rem_val-t+1)