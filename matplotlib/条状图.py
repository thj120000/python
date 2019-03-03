#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(1)
index= np.arange(5)
values= [5,7,3,4,6]
#bar()函数直接生成条状图
std1= [0.8,1,0.4,0.9,1.3]
plt.title('A Bar chart',color= 'red')
'''
设置一个std1误差列表，通过yerr和error_kw一起使用，然后传递误差参数
ecolor指定误差线的颜色，capsize指定误差线的宽度
'''
plt.bar(index,values,yerr= std1,error_kw={
    'ecolor':'green',
    'capsize':5},
        alpha=0.7,
        label='First',
        color='red'
        )
plt.xticks(index,['A','B','C','D','E'])
plt.legend(loc=2)
plt.show()

plt.figure(2)
plt.title('A horizontal Bar Chart')
plt.barh(index,values,xerr=std1,error_kw={
    "ecoloe":'red',
    'capsize':5},
         alpha=0.5,
         label='Second',
         color='blue'
)
plt.yticks(index,['a','b','c','d','e'])
plt.legend(loc=5)
plt.show()
