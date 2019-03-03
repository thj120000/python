#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

s= pd.Series([12,-4,7,9])
print (s,'\n')

s1= pd.Series([12,-4,7,9], index=['a','b','c','d'])
print (s1,'\n')
a=s1.values
b=s1.index
print (a,'\n')
print (b,'\n')

c=s1[0:2]
d=s1[['b','c']]
print (c,'\n')
print (d,'\n')
'''
用numpy定义新的Series对象
'''
arr= np.array([1,2,3,4])
s3= pd.Series(arr)
print (s3)
s4= pd.Series(s1)
print (s4)
'''
筛选元素
'''
s5=s4[s4>8]
print ('筛选后的元素剩余的元素：')
print (s5,'\n')
'''
Series 对象运算和数学函数
'''
s6= s1/2
print (s6,'\n')
'''
利用numpy中函数进行调用，需注明出处
'''
s7= np.log(s1)
print (s7,'\n')



