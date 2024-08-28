'''get the count of elements in a string which is not in another string


s1=input()
s2=input()
res=list(s2)
for i in res:
    if i in s1:
        res.remove(i)
print(len(res))
'''


strr=input()
ch1=input()
ch2=input()
strr=list(strr)
for i in range(len(strr)):
    if strr[i]==ch1:
        strr[i]=ch2
    elif strr[i]==ch2:
        strr[i]=ch1
print("".join(strr))

