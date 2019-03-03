#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data= {
    'series1':[1,3,4,5,3],
    'series2':[2,4,5,2,4],
    'series3':[3,2,3,1,2]
}
df= pd.DataFrame(data)
df.plot(kind= 'bar',stacked= True)#堆积利用的是stacked关键字
plt.show()