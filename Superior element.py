






arr=list(map(int,input().split()))
sup=arr[-1]
count=1
i=len(arr)-2
while i>=0:
    if arr[i]>sup:
        count+=1
        sup=arr[i]
    i=i-1
print(count)
