#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

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
frame3= frame1.add(frame2)
print (frame1,'\n')
print (frame2,'\n')
print(frame,'\n')
print(frame3,'\n')
'''
让Series对象的索引和Dataframe对象的列名保持一致，可以直接进行计算
'''
ser= pd.Series(np.arange(4),index=['ball','pen','pencil','paper'])
print(ser,'\n')
cha= frame1-ser
print (cha,'\n')
'''
如果不保持一致，则计算出来的结果为nan
'''
ser['mug']=9#添加一个元素
print (ser,'\n')
cha1= frame1-ser
print (cha1,'\n')

