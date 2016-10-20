

s=str(input().strip())
i=0
count=0
while(i<(s.__len__()-2)):

    temp=s[i:i+3]

    if(temp[0]!='S'):
        count=count+1
    if(temp[1]!='O'):
        count=count+1
    if(temp[2]!='S'):
        count=count+1
    i=i+3

print(count)







