'''str=input()
str1=""
for i in str:
    if i not in str1:
        str1=str1+i
for i in str1:
    count=str.count(i)
    print(i,":",count)'''
str=input()
d={}
for i in str:
    d[i]=str.count(i)
for i in d:
    print(i,":",d[i])