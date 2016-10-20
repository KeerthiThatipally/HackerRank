#!/bin/python3

import sys


s = input().strip()
s=s.upper().replace(" ",'')
print(s)
count = 1


list2 = []
[list2.append(i) for i in s if not i in list2]

if(list2.__len__()==26):
    print("pangram")
else:
    print("not pangram")