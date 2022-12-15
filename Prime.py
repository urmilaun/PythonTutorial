n=int(input("Enter a Number"))
if(n<2):
    print("not a prime number")
else:
    for i in range(2,n):
      if n%i==0:
        print("not a prime number")
    else:
        print("Prime number")