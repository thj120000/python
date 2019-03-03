#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

mydict = {'red':2000,'blue':1000,'yellow':500,'orange':1000}
myseries= pd.Series(mydict)
print (myseries,'\n')

'''
自定义索引
'''
colors= ['red','yellow','orange','blue','green']
myseries2= pd.Series(mydict,colors)
print (myseries2,'\n')