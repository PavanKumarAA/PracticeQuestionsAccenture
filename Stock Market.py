'''Find the elements lesser than the first element'''
'''
n=int(input())
arr=list(map(int,input().split()))
count=0
gre=arr[0]
for i in range(1,n):
    if i<gre:
        count+=1
print(count)
'''


t=list(map(int,input().split()))
l=[]
st=t[0]
for i in range(len(t)):
    if t[i]<st:
        l.append(t[i]-st)
        st=t[i]
print(l)