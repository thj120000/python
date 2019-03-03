#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data= pd.DataFrame(
    {
        'series1':[1,3,4,3,2],
        'series2':[2,4,5,2,4],
        'series3':[3,2,3,1,2]
    }
)
plt.figure(1)
data.plot(kind='bar')
plt.show()
plt.figure(2)
data.plot(kind='barh')
plt.show()