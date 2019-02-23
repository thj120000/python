#!@Author : Sanwat
#!@File : .py

import numpy as np

a= np.arange(10,16)
print(a)
a1= a[4]
print (a1)
a2= a[-1]
print (a2)
a3= a[-6]
print(a3)
a4= a[[1,3,4]]
print (a4)
'''
二维数组
'''
b= np.arange(10,19).reshape((3,3))
print(b)
b1= b[1,2]
print(b1)