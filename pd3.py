import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

data={
    "product_name":["pen","pencil","sugar","soap","pen","pencil","sugar","soap","pen","pencil","sugar","soap"],
    "years":[2000,2000,2000,2000,2001,2001,2001,2001,2002,2002,2002,2002],
    "profit":[10000,60000,50000,40000,30000,90000,70000,50000,40000,10000,30000,90000]


}

df=pd.DataFrame(data)

new=df.groupby(["product_name"])

for groupa,d in new:
    print(groupa)
    print(d)
    a=np.array(groupa)
    b=np.array(d)
print("Product name wise:",b)

pro=df.groupby("years")
for groupb,i in pro:
    print(groupb)
    print(i)
    y=np.array(groupb)
    x=np.array(i)
print("year wise",x)

pro=df.groupby("profit")
for groupc,x in pro:
    print(groupc)
    print(x)
    m=np.array(x)
    
pencil=input("enter the product name")
pencil_df=df[df["product_name"]==(pencil)]
plt.plot(pencil_df["years"],pencil_df["profit"])
df.plot(kind='bar',x='years',y='profit',color='red')
df.plot(kind='hist',x='years',y='profit',color='blue')
df.plot(kind='pie',x='years',y='profit')
plt.xlabel("years")
plt.ylabel("profit")
plt.title("graph")
plt.show()

