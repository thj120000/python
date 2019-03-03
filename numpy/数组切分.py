#!@Author : Sanwat
#!@File : .py
import numpy as np

a= np.arange(16).reshape((4,4))
print (a)
[a1,b1]= np.hsplit(a,2)
print (a1)
print (b1)

[a2,b2]= np.vsplit (a,2)
print (a2)
print (b2,'\n')

[a3,b3,c3]= np.split(a,[1,3],axis=1)
print (a3)
print (b3)
print (c3,'\n')

[a4,b4,c4]= np.split (a, [1,3], axis=0)
print (a4)
print (b4)
print (c4)