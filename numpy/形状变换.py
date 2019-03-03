#!@Author : Sanwat
#!@File : .py

import numpy as np

a= np.random.random(12)
print (a,'\n')

a1= a.reshape(3,4)
print (a1,'\n')

a.shape=(3,4)
print (a)

a2= a.ravel()
print(a2,'\n')
#交换行列的位置——即转置
a3= a.transpose()
print (a3)