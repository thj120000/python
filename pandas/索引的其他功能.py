#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

ser= pd.Series([2,5,7,4],index= ['one','two','three','four'])
print(ser,'\n')
'''
跟换索引对象
'''
ser2= ser.reindex(['three','four','five','one'])
print (ser2,'\n')
ser3= pd.Series([1,5,6,3],index=[0,3,5,6])
print(ser3,'\n')
'''
ffill,插入前面的值给后面；bfill插入后面的值给前面
'''
ser4= ser3.reindex(range(7),method='ffill')
print (ser4,'\n')
ser5= ser3.reindex(range(7),method='bfill')
print (ser5,'\n')
'''
删除索引drop函数
'''
ser6= ser.drop('three')
print (ser6,'\n')
'''
删除Dataframe中的元素，drop函数
'''
frame= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index= ['red','blue','yellow','white'],
    columns= ['ball','pen','pencil','paper']

)
print (frame,'\n')
frame1= frame.drop(['blue','yellow'])#删除blue和yellow两行
print (frame1,'\n')
frame2= frame.drop(['pen','pencil'],axis=1)
print (frame2,'\n')