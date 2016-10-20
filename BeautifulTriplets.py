n,d=input().strip().split(" ")
n=int(n)
d=int(d)
arr=[int(arr_temp) for arr_temp in input().strip().split(" ")]
count=0
for i in range(arr.__len__()-2):
    if arr[i]+d in arr:
        if arr[i]+(2*d)in arr:
            count=count+1
print(count)