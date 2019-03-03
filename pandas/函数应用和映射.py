#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

frame= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index= ['red','blue','yellow','white'],
    columns= ['ball','pen','pencil','paper']
)
frame1= np.sqrt(frame)
print (frame,'\n')
print(frame1,'\n')
'''
按照行或者列执行操作的函数
'''
'''
计算数组元素取值范围的函数lambda
'''
f= lambda x: x.max()-x.min()
frame2= frame.apply(f)
print (frame2,'\n')
'''
方法二：定义函数
'''
def ff(x):
    return x.max()-x.min()
frame3= frame.apply(ff)#处理行
print(frame3,'\n')
frame4= frame.apply(ff,axis=1)#处理列
print (frame4,'\n')

'''
利用apply 函数返回Series 对象和Dataframe 对象
'''
def fff(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])
frame5= frame.apply(fff)#行的最小值和最大值
print(frame5,'\n')
frame6= frame.apply(fff,axis=1)#列的最小值和最大值
print (frame6,'\n')
'''
统计函数
'''
frame7= frame.sum()
print (frame7,'\n')
frame8= frame.mean()
print (frame8,'\n')
frame9= frame.describe()#能够计算多个统计量
print(frame9,'\n')


