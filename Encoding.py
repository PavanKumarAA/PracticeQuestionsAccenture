'''
s=input()
res=''
for i in s:
    res+=chr(ord("a")+ord("z")-ord(i))
print(res)



s=input().lower()
res=""
for i in s:
    if(ord(i)<ord("v")):
        res+=chr(ord(i)+5)
    else:
        res+=chr(ord(i)+5-26)
print(res)

import string
s=list(string.ascii_lowercase)
ss=input()
res=0
for i in range(len(s)):
    if s[i] in ss:
        res+=i+1
print(res)



s=input().lower()
res=0
for i in s:
    res=res+(ord(i)-96)
print(res)

def fib(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
s=input()
summ=0
for i in s.lower():
    val=fib(ord(i)-96)
    summ+=val
print(summ)




s=input()
res=1
for i in s:
    if i.isdigit():
        res=res*int(i)
print(res)
'''


'''reverse a number without converting it to string'''
'''
num=int(input())
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
'''
'''if in a string there are consecutive numbers make them as multinumber and then get the sum of the given numbers 


s=input()
res=0
num=0
for i in s:
    if i.isdigit():
        num=num*10+int(i)
    else:
        res+=num
        num=0
res+=num
print(res)
'''
