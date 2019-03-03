#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

'''
跟pandas 数据结构（series 和 Dataframe ）中其他元素不同的是，index对象不可改变
'''
ser= pd.Series([5,0,3,8,4],index=['red','blue','yellow','white','green'])
index= ser.index
print(index,'\n')
'''
返回最大值和最小值
'''
min= ser.idxmin()
max= ser.idxmax()
print (min,'\n')
print (max,'\n')
'''
具有重复标签的index
'''
serd= pd.Series(range(6),index= ['white','white','blue','green','green','yellow'])
print(serd,'\n')
serd1= serd['white']
print (serd1,'\n')
s=serd.index.is_unique
print (s,'\n')