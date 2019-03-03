#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

s1= pd.Series([3,2,5,1],['white','yellow','green','blue'])
s2= pd.Series([1,4,7,2,1],['white','yellow','black','blue','browm'])
s= s1+s2
print (s,'\n')
'''
Dataframe对象之间的数据对齐与计算
'''
frame1= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index= ['red','blue','yellow','white'],
    columns= ['ball','pen','pencil','paper']
)
frame2= pd.DataFrame(
    np.arange(12).reshape((4,3)),
    index= ['blue','green','white','yellow'],
    columns= ['mug','pen','ball']
)
frame= frame1+frame2
print (frame1,'\n')
print (frame2,'\n')
print(frame,'\n')