data=[{"s_id":1,"s_name":"Maharashtra","cities":[{"c_id":1,"c_name":"Pune","location":[{"l_id":2,"l_name":"Hadapsar"}]}]}]
for s in data:
    print(str(s["s_id"])+"  "+s["s_name"])
    for c in s["cities"]:
        print("     "+str(c["c_id"])+"  "+c["c_name"])
        for i in c["location"]:
            print("         "+str(i["l_id"])+"  "+i["l_name"])
    print("-----------------------------------------------")