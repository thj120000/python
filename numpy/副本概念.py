#!@Author : Sanwat
#!@File : .py
import numpy as np

a= np.array([1,2,3,4])
b= a
print (b)
a[2]=0
print ("修改a后，副本b为：\n",b)

c= a[0:2]
print (c)
a[0]=0
print (c)

A=np.array([1,2,3,4])
d= A.copy()
print (d)
A[0]=0
print (d)#副本保留不变