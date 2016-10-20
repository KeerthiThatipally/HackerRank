n=int(input().strip())


for i in range(n):
    a=int(input().strip())

    count = 0
    c=[int(arr_temp) for arr_temp in input().strip().split(' ')]
    for i in range(a):
        sum_l = 0
        sum_r = 0
        for j in range(0,i):
            sum_l=sum_l+c[j]

        k=0
        for k in range(i+1,a):
            sum_r=sum_r+c[k]

        if(sum_l==sum_r):
            count=1
            break
    if(count==1):
        print("YES")
    else:
        print("NO")


