#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

ser= pd.Series([5,0,3,8,4],index= ['red','blue','yellow','white','green'])
print (ser,'\n')
'''
sort_index函数：各索引按照字母表升序（A-Z)的标签进行排序
'''
ser2= ser.sort_index()
print (ser2,'\n')
ser3= ser.sort_index(ascending=False)
print(ser3,'\n')

frame= pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index= ['red','blue','yellow','white'],
    columns= ['ball','pen','pencil','paper']
)
print (frame,'\n')
frame1= frame.sort_index()#按行进行升序
print (frame1,'\n')
frame2= frame.sort_index(axis= 1)#按列进行升序
print (frame2,'\n')

'''
接下来对元素进行排序

ser1= pd.Series([5,0,3,8,4],index= ['red','blue','yellow','white','green'])
print (ser1,'\n')
ser4= ser.order()
print (ser4,'\n')
'''
frame3= frame.sort_index(by= 'pen')
print (frame3,'\n')
frame4= frame.sort_index(by= ['pen','pencil'])
print(frame4,'\n')

'''
位次排序
'''
ser5= ser.rank()
print (ser5,'\n')
ser6= ser.rank(ascending=False)
print (ser6,'\n')