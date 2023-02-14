# class MyName:
#     def Addition(self):
#         print("calling a default class")

#     def Addition(self,a):
#         print("calling a one argument class")

#     def Addition(self,a,b):
#         print("Calling with two argument")

#     def Addition(self,a,b,c):
#         print("calling with three argument")

# m=MyName()
# # m.Addition(10)
# # m.Addition(10,20)
# m.Addition(10,20,30)

class abc:
    def Add(self,a,b):
        c=a+b
        print(c)

class xyz(abc):
    def sub(self,m,n):
        c=m-n
        print(c)

x=xyz()
# x.sub(10,20)
x.Add(30,40)
