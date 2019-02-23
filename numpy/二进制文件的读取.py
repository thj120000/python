#!@Author : Sanwat
#!@File : .py
import numpy as np

a= np.random.random((4,4))
print (a,'\n')
np.save('tang_save',a)

b= np.load('tang_save.npy')
print (b,'\n')