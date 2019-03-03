#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

Data = {'color':['blue','green','yellow','red','white'],
        'object':['ball','pen','pencil','paper','mug'],
        'price':[1.2,1.0,0.6,0.9,1.7]
}
frame= pd.DataFrame(Data)
print (frame,'\n')
'''
选择其中的指定部分，例如只选择object,和price项
'''
frame2= pd.DataFrame(Data,columns=['object','price'])
print (frame2,'\n')
'''
自定义索引部分
'''
frame3= pd.DataFrame(Data,index=['one','two','three','four','five'])
print (frame3,'\n')
'''
定义构造函数生成数据库
'''
frame4= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper']
)
print(frame4,'\n')
