#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
frame1= pd.DataFrame(
    np.arange(9).reshape(3,3),
    index=['white','black','red'],
    columns=['ball','pen','pencil']
)
print (frame1,'\n')
'''
入栈（stacking）：旋转数据结构，把列转换成行
出栈（unstacking):把行转换成列
'''
stack1= frame1.stack()#入栈
print (stack1,'\n')
unstack1= stack1.unstack()
print (unstack1,'\n')

'''
从‘长’格式向‘宽’格式转换
'''
longframe= pd.DataFrame(
    {
        'color':['white','white','white','color','color','color','black','black','black'],
        'item':['ball','pen','mug','ball','pen','mug','ball','pen','mug'],
        'value':np.random.rand(9)
    }
)
print (longframe,'\n')
'''
利用pivot()函数将一列或者多列作为参数
'''
wideframe= longframe.pivot('color','item')
print (wideframe,'\n')
'''
删除多余的行和列
'''
del frame1['ball']#删除多余的列，利用del命令
print (frame1,'\n')
frame2= frame1.drop('white')#删除多余的行，利用drop()函数
print(frame2,'\n')