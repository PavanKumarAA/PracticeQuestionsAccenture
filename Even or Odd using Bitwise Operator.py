'''Even or Odd using bitwise operator


n=int(input())
if(n&1):
    print("Odd number")
else:
    print("Even number")
'''

'''Toggle the kth bit of a number'''
n=int(input())
k=int(input())
res=n^(1<<(k-1))
print(res)
res1=n & (~(1<<(k-1)))
print(res1)

