state=[]
i=1
cid=1
sid=1

while(i!=0):
    sname=input("Enter the state name")
    city=[]
    c=1
    while(c!=0):
        cname=input("Enter city")
        ct={"city_id":cid,"city_name":cname}
        city.append(ct)
        cid+=1
        c=int(input("Do you wants to add more city?Yes(1)/No(0)"))
    st={"state_id":sid,"state_name":sname,"city":city}
    state.append(st)
    sid+=1
    i=int(input("Do you wants to add more state?Yes(1)/No(0)"))



print("My Data")
for s in state:
    print(str(s["state_id"])+" "+s['state_name'])
    for c in s["city"]:
            print("              "+str(c["city_id"])+" "+c['city_name'])
    print("---------------------------------------------------------")

