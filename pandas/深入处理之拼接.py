#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
'''
numpy 中的concatenate 函数就是用于数组的拼接操作
'''

array1= np.arange(9).reshape((3,3))
print(array1,'\n')
array2= np.arange(9).reshape((3,3))+6
print (array2,'\n')
array3= np.concatenate([array1,array2],axis=1)#横向拼接
print (array3,'\n')
array4= np.concatenate([array1,array2],axis=0)#纵向拼接
print (array4,'\n')
'''
pandas 库以及他的Series 和Dataframe 等数据结构实现了带编号的轴，他可以进一步扩展数组的拼接功能.
利用的pandas 中的concat函数
'''
ser1= pd.Series(
    np.random.rand(4),index=[1,2,3,4]
)
print (ser1,'\n')
ser2= pd.Series(
    np.random.rand(4),index=[5,6,7,8]
)
print (ser2,'\n')
ser3= pd.concat([ser1,ser2])#默认情况是按照axis=0,即按列进行拼接的
print (ser3,'\n')
#横向拼接的话，axis=1即可
ser4= pd.concat([ser1,ser2],axis=1)
print (ser4,'\n')
"""
由于刚才的结果无重合数据，是外拼接。把join选项设置为inner,可以执行内连接操作
"""
ser5= pd.concat([ser1,ser2],axis=1,join='inner')
print (ser5,'\n')
'''
在拼接的轴上面，创建等级索引
'''
ser6=pd.concat([ser1,ser2],keys=[1,2])
print (ser6,'\n')
'''
按行拼接的话
'''
ser7= pd.concat([ser1,ser2],keys=[1,2],axis=1)
print(ser7,'\n')
'''
接下来，拼接DATAframe 
'''

frame1= pd.DataFrame(
    np.random.rand(9).reshape(3,3),
    index=[1,2,3],
    columns=['A','B','C']
)

frame2= pd.DataFrame(
    np.random.rand(9).reshape(3,3),
    index=[4,5,6],
    columns=['A','B','C']
)
frame3= pd.concat([frame1,frame2])
print (frame3,'\n')
frame4= pd.concat([frame1,frame2],axis=1)
print(frame4,'\n')
'''
组合数据，例如两个数据集的索引完全或部分重合，则可以利用combine_first()函数组合Series对象，同时对齐数据
'''

sser1= pd.Series(
    np.random.rand(5),
    index=[1,2,3,4,5]
)
sser2= pd.Series(
    np.random.rand(4),
    index=[2,4,5,6]
)
sser3= sser1.combine_first(sser2)
print (sser3,'\n')
sser4= sser2.combine_first(sser1)
print (sser4,'\n')

'''
部分合并
'''
sser5= sser1[:3].combine_first(sser2[:3])
print (sser5,'\n')