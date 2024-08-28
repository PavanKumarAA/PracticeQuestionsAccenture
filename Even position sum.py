'''for doing this we've take the index as odd as it starts from 0,if it is one based do it normally'''
arr=list(map(int,input().split()))
arr.reverse()
sum=0
for i in range(len(arr)):
    if i%2==0:
        sum+=arr[i]
print(sum)

