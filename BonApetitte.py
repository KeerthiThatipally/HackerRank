n,k = input().strip().split(' ')

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

n1=int(input().strip())
sum=0
n=int(n)
k=int(k)
for i in range(0,n):
    sum=sum+arr[i]

diff=int((sum-arr[k])/2)


if(diff==n1):
    print("Bon Appetit")
else:
    print(n1-diff)