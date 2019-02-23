#!@Author : Sanwat
#!@File : .py
import numpy as np
a=np.array([1,2,3,4,5])
print(a)
x=2
b=np.zeros(len(a)+(len(a)-1)*x)
b[::x+1]=a
print(b)