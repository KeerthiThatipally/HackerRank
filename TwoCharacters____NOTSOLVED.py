#!/bin/python3

import sys


s_len = int(input().strip())
s = input().strip()


isValid=False
for i in range(s_len-2):
    if not (s[i]==s[i+2]):
       break
    else:
        isValid=True




if not (isValid):
    max = 0
    for i in range(0,s_len-2):
        count=0

        temp=list(s)
        temp = list(filter(lambda x: x!= s[i], s))

        for j in range(temp.__len__()-2):
            if not (temp[j]==temp[j+2]):
                break
            else:
                count=count+1

        if(count==temp.__len__()-2):
            len=temp.__len__()
            print("len:"+len)
            if (len > max):
                max = len
    print(max)


else:
    print(s_len)


