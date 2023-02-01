class Teacher:
    tid=""
    tname=""
    def setdata(self,a,b):
        self.tid=a
        self.tname=b
    def getdata(self,a,b):
        print(self.tid)
        print(self.tname)
    
class Student:
    rollno=""
    sname=""
    def putdata(self,x,y):
        self.rollno=x
        self.sname=y
    def printdata(self):
        print(self.rollno)
        print(self.sname)