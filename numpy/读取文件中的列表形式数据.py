#!@Author : Sanwat
#!@File : .py
import numpy as np

data= np.genfromtxt('data.csv.txt',delimiter=',',names=True)
print (data,'\n')

data2= np.genfromtxt('data2.txt',delimiter=',',names=True)
print (data2)
co1= data2['id']
print ('列抽取：',co1,'\n')
ro1= data2[0]
print('行抽取：',ro1,'\n')