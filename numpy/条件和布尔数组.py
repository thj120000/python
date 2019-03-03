#!@Author : Sanwat
#!@File : .py
import numpy as np

a= np.random.random((4,4))
print (a,'\n')
a1= a[a<0.5]
print (a1)