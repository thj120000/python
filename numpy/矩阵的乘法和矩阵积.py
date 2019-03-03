#!@Author : Sanwat
#!@File : .py
import numpy as np

'''
矩阵的乘法
'''
a= np.arange(0,9).reshape(3,3)
print (a)

b= np.ones((3,3))
print (b)
'''
该方法只在numpy中能用，如果在python中需要这样做
一维：
for (i=0;i<rows;i++){
    c[i]=a[i]*b[i];
    }
二维矩阵相乘：
for (i=0;i<rows;i++){
    for （j=0;j<columns;j++){
        c[i][j]=a[i][j]*b[i][j];
        {
    }
'''
c= a*b
print (c)

'''
矩阵积1
'''
d= np.dot (a,b)
print (d)
'''
矩阵积2
'''
e= a.dot(b)
print(e)

f= b.dot(a)
print (f)