t1,t2,n=input().strip().split(" ")
t1,t2,n=[int(t1),int(t2),int(n)]
arr=[0]*n
arr[0]=t1
arr[1]=t2

if(n==1):
    print(t1)
elif(n==2):
    print(t2)
for i in range(2,n):
    if(arr[i]==0):
        arr[i]=arr[i-2]+(arr[i-1]**2)

print(arr[n-1])

