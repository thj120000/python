#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= {
    'series1':[1,2,3,4,5],
    'series2':[2,3,4,5,1],
    'series3':[3,2,3,1,2]
}
df= pd.DataFrame(data)
x=np.arange(0,5)
plt.axis([0,5,0,6])
plt.plot(x,df)
plt.legend(data,loc=2)
plt.show()