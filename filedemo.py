# f=open("myfile.txt","a")
# # f.write("for i in range(1,11):\nsqu=i*i\nprint(squ)\n")
# for i in range(1,101):
#     f.write("Square of "+str(i)+"="+str(i*i)+"\n")

#f=open("myfiledemo.txt","a")
#f.write("welcome\n")

f=open("myfile.txt","r")
cnt=0
data=f.read()
for d in data:
    if(d=="1"):
        cnt+=1
print("Count of 1="+str(cnt))









