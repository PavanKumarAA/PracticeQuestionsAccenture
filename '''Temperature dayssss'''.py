'''Temperature dayssss'''

t=list(map(int,input().split()))
res=[0 for x in range(len(t))]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[j]>t[i]:
            res[i]=j-i
            break
print(res)