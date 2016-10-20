t=int(input().strip())
for i in range(t):
    m=int(input().strip())
    n=int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    for i in range(0,n):
        for j in range(1,n):
            if(a[i]+a[j]==m and i<j):
                print(str(i+1)+" "+str(j+1))