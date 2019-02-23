#!@Author : Sanwat
#!@File : .py
import numpy as np

a=np.ones((3,3))
b=np.zeros((3,3))
print (a)
print (b)

c= np.vstack((a,b))
d= np.hstack((a,b))
print ('数组垂直压入：\n',c,'\n')
print ('数组水平压入：\n',d,'\n')

'''
接下来两个函数是把一维数组作为列或行压入栈结构
'''
a1= np.array([0,1,2])
b1= np.array([3,4,5])
c1= np.array([6,7,8])
a2= np.column_stack((a1,b1,c1))
a3= np.row_stack((a1,b1,c1))
print ('将三个一维数组按照列压入栈：')
print (a2)
print ("将三个一维数组按照行压入栈：")
print (a3)