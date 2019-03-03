#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

serd = pd.Series([1,0,2,1,2,3],index= ['white','white','blue','green','green','yellow'])
print (serd,'\n')
a= serd.unique()#只剩下其中的单一元素
print (a,'\n')
b= serd.value_counts()
print (b,'\n')#筛选出其中的单一元素，并显示出个数
c= serd.isin([0,3])
print (c,'\n')
d= serd[serd.isin ([0,3])]
print (d,'\n')