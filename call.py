from  bank import Customers
c=Customers()
i=1
while(i!=0):
    ch=int(input("Enter the Choice:\n1. adduser\n2.Logic"))
    if(ch==1):
        c.adduser()
    elif(ch==2):
        c.Logic()
        
    


    
