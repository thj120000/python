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
print (frame,'\n')
'''
1,利用groupby()计算一列的均值
'''
group= frame['price1'].groupby(frame['color'])
print (group,'\n')
result= group.groups
print (result,'\n')
mean= group.mean()
print (mean,'\n')
s= group.sum()
print (s,'\n')
'''
同理：根据产品计算
'''
group1= frame['price2'].groupby(frame['object'])
print (group1,'\n')
mean1= group1.mean()
print (mean1,'\n')
s2=group1.sum()
print (s2,'\n')

'''
2,等级分组
'''
group2= frame['price1'].groupby([frame['color'],frame['object']])
print (group2.mean(),'\n')
print (group2.sum(),'\n')

group3=frame[['price1','price2']].groupby([frame['color'],frame['object']])
print (group3.mean(),'\n')
print (group3.sum(),'\n')

group4= frame[['price1','price2']].groupby(frame['color'])
print (group4.mean())