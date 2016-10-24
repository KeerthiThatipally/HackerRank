n,k=input().strip().split(" ")
n=int(n)
k=int(k)


min=0
sum=0
list=[]
for i in range(n):

    l,t=input().strip().split(" ")
    l=int(l)
    t=int(t)
    if(t==1):
        list.append(l)
    else:
        sum=sum+l


list.sort()
temp=0
for i in list[::-1]:

    if(temp<k):
        temp=temp+1
        sum=sum+int(i)
    else:
        sum=sum-int(i)






print(sum)