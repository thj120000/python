#!@Author : Sanwat
#!@File : .py

import numpy as np

a= np.arange(10,16)
print (a)
a1=a[1:5]
print (a1)
a2= a[1:5:2]
print (a2)
a3= a[::2]
print(a3)
a4= a[:5:2]
print(a4)
a5= a[:5:]
print (a5,'\n','\n','二维数组：')

'''
二维数组
'''
b= np.arange(10,19).reshape((3,3))
print(b)
b1= b[0,:]  #第0行元素
print(b1)
b2= b[:,0] #第0列元素
print (b2)
b3= b[0:2,0:2]
print (b3)

'''
该段表示取第0行和第2行的第0号和第一号元素
'''
b4= b[[0,2],0:2]
print (b4)

