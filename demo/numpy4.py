#!@Author : Sanwat
#!@File : .py
import numpy as np
a=np.array([[0,1,2,3],[4,5,6,7]])
print (a)
x= 5.1
a= abs(a-x)
print(a)
b= a.min ()
c= abs(x-b)
print("这个数组中最接近5.1的数为：",c)