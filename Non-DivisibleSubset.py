n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
arr=[int(arr_temp) for arr_temp in input().split(' ')]
arr_res=[]

for i in range(n):
    for j in range(i+1,n):
        if(((arr[i]+arr[j])%k)!=0):
            arr_res.append(arr[i])
            arr_res.append(arr[j])


print(set(arr_res))
print(set(arr_res).__len__())