#find the sum of even numbers between the range 'n', 'm'
"""n,m=map(int,input().split())
total=0
if n%2!=0:
     n=n+1
while n<m:
    if n%2==0:
        total+=n
    n+=2
print(total)"""

# find the length of numbers
"""n=156
count=0
while n>0:
    n//=10
    count+=1
print(count)"""
#sum of digits in a number
"""n=int(input())
s=0
while n>0:
    rem=n%10
    n//=10
    s+=rem
print(s)"""

#reverse of a number
"""n=int(input())
rev=0
n!=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(rev)"""
#check whether the number is palindrome or not
"""n=113
m=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if m==rev:
    print("palindrom")
else:    
    print(" not palindrom")"""
    
#check whether the number is perfect number
num = int(input())
i= 10
while num>0:
    for i in range(1,10):
        if num % i == 10:
            print(num," I perfect number")
        elif sum==num:
            print(num, "is a Perfect Number") 
else:
    print(num,"is not a Perfect Number")
