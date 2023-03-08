import numpy as np
import pandas as pd

st={"rollno":[1,2,3,4,5],
    "name":["Urmila","Rushika","Kirti","pooja","shruti"],
    "Designation":["student","employee","manager","hr","CEO"],
    "salary":[100000,200000,30000,400000,50000]}

df=pd.DataFrame(st)

data=df.groupby("Designation")

for group,dt in data:
    print(group)
    print(dt)


