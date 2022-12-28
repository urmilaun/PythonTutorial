n=153
s=n
b=len(str(n))
sum=0
while(n!=0):
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==sum:
    print("number is armstrong")
else:
    print("the number is not armstrong")