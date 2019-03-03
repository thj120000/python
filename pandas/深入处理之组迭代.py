#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

frame= pd.DataFrame(
    {
        'color':['white','red','green','red','green'],
        'object':['pen','pencil','pencil','ashtray','pen'],
        'price1':[5.56,4.20,1.30,0.56,2.75],
        'price2':[4.75,4.12,1.60,0.75,3.15]
    }
)
for name ,group in frame.groupby('color'):
    print (name)
    print (group)
'''
1,链式转换
'''
result1= frame['price1'].groupby(frame['color']).mean()
print (result1,'\n')
type1=type(result1)
print(type1,'\n')
result2= frame.groupby(frame['color']).mean()
print (result2,'\n')
type2=type(result2)
print (type2,'\n')

'''
quantile()计算分位数
'''
group= frame.groupby('color')
print (group['price1'].quantile(0.6))
'''
自定义聚合函数
定义好函数后，将其作为参数传给agg（）函数。
'''
def range (series):
    return series.max()-series.min()
chazhi= group['price1'].agg(range)
print (chazhi,'\n')

print ('对整个组用：','\n')
print (group.agg(range),'\n')

print (group['price1'].agg(['mean','std',range]))