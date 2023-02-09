import mysql.connector
class Customers():
    def adduser(self):    
        n=input("Enter the customer name")
        acc_num=int(input("Enter the account number"))
        mob_num=input("Enter the mobile number")
        email=input("Enter the email id")
        acc_type=input("enter the account_type")
        acc_bal=input("Enter the account balance")
        password=input("Enter the password")
        con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")
        mycursor=con.cursor()
        mycursor.execute("insert into customers(customer_name,account_number,mobile_number,email,account_type,account_balance,password) values('"+n+"',"+str(acc_num)+",'"+str(mob_num)+"','"+str(email)+"','"+str(acc_type)+"',"+str(acc_bal)+",'"+str(password)+"')")
        con.commit()
        print("Successfully added")

   def Logic(self):
        a=int(input("enter account number"))
        p=input("enter password")
        con=mysql.connector.connect(host="localhost",user="root",password="",database="bank")
        mycursor=con.cursor()
        mycursor.execute("select * from customer where account_number="+str(a)+"and password="+p+"")
        data=mycursor.fetchall()
        if(len(data)>0):
            print(data)
        else:
            print("Check the account number and password")
