#!@Author : Sanwat
#!@File : .py
import numpy as np

a= np.arange(16).reshape(4,4)
b= np.arange(4)
print (a,'\n')
print (b,'\n')
s= a+b
print (s,'\n')

'''
维度为：3*1*2
'''
m= np.arange(6).reshape(3,1,2)
print ('m为：')
print (m,'\n')
'''
维度为：3*2*1
'''
n= np.arange(6).reshape(3,2,1)
print ('n为：')
print(n,'\n')

ss= m+n
print(ss)


