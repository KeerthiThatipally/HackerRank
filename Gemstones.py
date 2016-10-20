n=int(input().strip())
arr=[0]*26

list=[]
for i in range(n):
    s=input().strip()
    list.append(s)

for i in list:
    for j in set(i):

        k=ord(j)-ord("a")
        arr[k]=arr[k]+1

count=0
for i in arr:
    if(i==n):
        count=count+1
print(count)



