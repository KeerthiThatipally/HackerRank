n=int(input().strip())
m=5
sum=0
for i in range(0,n):
    sum=sum+int(m/2)
    m=int(m/2)*3

print(sum)