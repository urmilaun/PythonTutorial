qualifications=[]
i=1
spid=1
qid=1

while(i!=0):
    qname=input("Enter Qualification")
    specializations=[]
    p=1
    while(p!=0):
        spname=input("Enter Specialization")
        st={"specialization_id":spid,"specialization_name":spname}
        specializations.append(st)
        spid +=1
        p=int(input("Do you wants to add more specializations?Yes(1)/No(0)"))
    qt={"qualification_id":qid,"qualification_name":qname,"specializations":specializations}
    qualifications.append(qt)
    qid+=1
    i=int(input("Do you wants to add more qualifications?Yes(1)/No(0)"))



print("My Data")
for q in qualifications:
    print(str(q["qualification_id"])+" "+q['qualification_name'])
    for s in q["specializations"]:
            print("              "+str(s["specialization_id"])+" "+s['specialization_name'])
    print("---------------------------------------------------------")