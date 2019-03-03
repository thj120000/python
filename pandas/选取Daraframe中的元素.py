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
选择所有列的名称
'''
frame2= frame.columns
print(frame2,'\n')
'''
选择所有列表的索引，即所有行的名称
'''
frame3= frame.index
print (frame3,'\n')
'''
选取列表中的所有的值
'''
frame4= frame.values
print (frame4,'\n')
'''
选择列表中的特定列
'''
frame5= frame['price']
print (frame5,'\n')
frame6= frame.object
print (frame6,'\n')
'''
选择列表中的行元素
'''
frame7= frame.ix[2]
print (frame7,'\n')
'''
指定多行元素
'''
frame8= frame.ix[[2,4]]
print (frame8,'\n')
'''
利用矩阵的性质选取区域
'''
frame9 = frame[1:3]#选取1，2两行
print(frame9,'\n')
'''
获取矩阵中的单个元素
'''
frame10 = frame['object'][3]
print (frame10,'\n')



