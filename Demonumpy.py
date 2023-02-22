import numpy as np
from matplotlib import pyplot as plt
r=[]
m=[]
i=1
while(i!=0):
    a=int(input("Enter the roll no"))
    b=int(input("Enter the Marks"))
    r.append(a)
    m.append(b)
    i=int(input("Do you want add more yes(1) no(0)"))
x=np.array(r)
y=np.array(m)
plt.plot(x,y,"or")
plt.show()