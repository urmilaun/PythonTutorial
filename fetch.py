import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="studentdb")
mycursor=con.cursor()
mycursor.execute("select * from student")
data=mycursor.fetchall()
##print(data)

for d in data:
    print(str(d[0])+""+str(d[1])+""+str(d[2])+""+str(d[3]))
