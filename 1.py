import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
data=[10,20,30,40,50,60]
x=np.array(data)
df=pd.Series(data,index=[10,20,30,40,50,60])
print(df[20])