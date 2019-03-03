#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

s= pd.Series([5,-3,np.NaN,14])
print (s,'\n')
s1= s.isnull()
print (s1,'\n')
s2= s.notnull()
print (s2,'\n')
'''
筛选NaN元素和相反元素
'''
s3= s[s.isnull()]
print (s3,'\n')
s4= s[s.notnull()]
print (s4,'\n')
