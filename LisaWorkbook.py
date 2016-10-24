n,k= input().strip().split(' ')
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

n=int(n)
k=int(k)

count =0
page=0

for i in range(0,arr.__len__()):
    j=0
    page=page+1
    for j in range(arr[i]):
        if (j !=0 and j%k == 0):
            page = page + 1
        if (j+1 == page):
            count =count+ 1



print(count)