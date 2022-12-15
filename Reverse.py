import math
n=int(input("Enter a number"))
temp=n
sum=0
while n!=0:
  rem=n%10
  sum=rem+sum*10
  n=math.floor(n/10)
print(sum)
