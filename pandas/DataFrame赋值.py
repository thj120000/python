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
frame.index.name= 'id'
frame.columns.name= 'item'
print (frame,'\n')
'''
添加新的列
'''
frame['new']=12
print (frame,'\n')
frame ['new']=['9.2','1.3','4.5','5.6','9.8']
print (frame,'\n')
'''
添加series
'''
ser= pd.Series(np.arange(5))
print (ser,'\n')
frame['new']=ser
print (frame,'\n')
'''
修改单个元素
'''
frame['price'][2]=3.3
print(frame,'\n')

'''
元素所属关系
'''
frame1= frame.isin([1.0,'pen'])
print(frame1,'\n')
frame2= frame[frame.isin([1.0,'pen'])]
print (frame2,'\n')
'''
删除一列
'''
del frame['new']
print (frame,'\n')
'''
筛选特定值大小的元素
'''
frame4= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper']
)
print(frame4,'\n')
frame5= frame4[frame4<12]
print (frame5,'\n')
'''
利用字典的嵌套生成Dataframe对象
'''
nestdict= {
    'red':{2012:22,2013:33},
    'white':{2011:13,2012:22,2013:16},
    'blue':{2011:17,2012:27,2013:18}
}
frame6= pd.DataFrame(nestdict)
print (frame6,'\n')
'''
Dataframe转置
'''
frame7= frame6.T
print (frame7,'\n')
frame8= frame4.T
print(frame8,'\n')

