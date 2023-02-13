class Parent:
    a=0
    b=0
    def __init__(self,x,y):
        self.a=x
        self.b=y
        print("Calling parent class")

    def Add(self):
        c=self.a+self.b
        print("Add",c)

class Child(Parent):
    p=0
    q=0
    def __init__(self, m, n):
        self.p=m
        self.q=n
        super().__init__(m,n)

        print("Calling child class")
    def Sub(self):
        c=self.p-self.q
        print("sub",c)

class subchild(Child):
    e=0
    f=0
    def __init__(self, h, i):
     self.e=h
     self.f=i
    def multi(self):
        c=self.e*self.f
        print("multi",c)


c1=subchild(10,20)
c1.Add()
c1.Sub()
c1.multi()       
