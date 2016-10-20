n=int(input().strip())
s=''

for i in range(n):
    isNotFunny = False
    s=input().strip()
    r=s[::-1]


    for j in range(1,s.__len__()-1):
        if not ((abs(ord(s[j])-ord(s[j-1])))==(abs(ord(r[j])-ord(r[j-1])))):

            isNotFunny=True

    if(isNotFunny==True):
        print("Not Funny")
    else:
        print("Funny")








