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
