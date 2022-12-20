msg="Welcome To Pune"
data=""
for i in range(len(msg)-1,-1,-1):
    if(msg[i]!=' '):
        data=msg[i]+data
    else:
        print(data,end=" ")
        data=""
print(data)