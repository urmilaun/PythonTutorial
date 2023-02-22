import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data=[10,20,30,40,50]
x=np.array(data)
print(x)

rno=[1,2,3,4,5,6]
name=["Urmila","Rushika","Viru","Akash","Pooja","Suraj"]
maths=[89,45,67,88,67,78,]
eng=[76,78,89,76,89,78]
sci=[78,89,90,78,89,78]
st={"rollno":rno,"name":name,"mathes":maths,"english":eng,"science":sci}
df=pd.DataFrame(st,columns=["rollno","name","mathes","english","science",])
print(df)
df["total"]=df["mathes"]+df["english"]+df["science"]
df["percentage"]=df["total"]/3
df["result"]=df["percentage"].apply(lambda x:'pass' if x>40 else 'fail')
print(df)


plt.show()

