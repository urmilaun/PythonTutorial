import math
n=(int(input("enter a number")))
temp=n
sum=0
while n>0:
  rem=n%10
  sum=rem+sum*10
  n=math.floor(n/10)
if temp==sum:
    print(" Palindrome")
else:
    print(" not Palindrome")