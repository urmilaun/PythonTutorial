class Calculation:
    x=0
    y=0
    def __init__(self,x,y):
            self.a=x
            self.b=y
    def addition(self):
        c=self.a+self.b
        print("addition is",c)
    def substraction(self):
        c=self.a-self.b
        print("substraction is",c)
    def multiplication(self):
        c=self.a*self.b
        print("multiplication is",c)
    def division(self):
        c=self.a/self.b
        print("division is ",c)
