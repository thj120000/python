#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= {
    'series1':[1,3,4,3,5],
    'series2':[2,4,5,2,4],
    'series3':[3,2,3,1,3]
}
df= pd.DataFrame(data)
'''
每一幅图只能表示出一个序列，所以只能选择了series1 作为表示
'''
df['series1'].plot(kind= 'pie',figsize=(6,6))
plt.show()