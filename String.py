msg="Welcome to Pune"
data=""
for m in msg:
    if(m!=""):
        data=m+data
    else:
        print(data,end="")
        data=""
print(data)


        
    