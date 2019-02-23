#!@Author : Sanwat
#!@File : .py
# -*- coding: UTF-8 -*-

import numpy as np

a= np.arange(10,16)
print (a)
for i in a:
    print (i)

b= np.arange(10,19).reshape((3,3))
for row in b:
    print (row)
#遍历每一个元素
for item in b.flat:
    print (item)

a1=np.apply_along_axis(np.mean,axis=0,arr=b)
print(a1)
a2=np.apply_along_axis(np.mean, axis=1, arr=b)
print (a2)

def foo(x):
    return x/2
a3=np.apply_along_axis(foof, axis=0, arr=b)
print("按行遍历处理：\n",a3)
a4=np.apply_along_axis(foo, axis=1, arr=b)
print ("按列遍历处理：\n",a4)
