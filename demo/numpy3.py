#!@Author : Sanwat
#!@File : .py
import numpy as np

Z = np.random.random((5,5))
print(Z,"\n")
max=Z.max()
min=Z.min()
print(max,min,'\n')
Z=(Z-min)/(max-min)
print(Z)