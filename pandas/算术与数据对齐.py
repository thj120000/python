#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

s1= pd.Series([3,2,5,1],['yellow','white','blue','green'])
s2= pd.Series([1,4,7,2,1],['yellow','white','black','blue','brown'])

s= s2+s1
print (s,'\n')

frame1= pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns= ['ball','pen','pencil','paper'])
frame2= pd.DataFrame(np.arange(12).reshape((4,3)),
                     index=['blue','green','white','yellow'],
                     columns=['mug','pen','ball'])
print(frame1,'\n')
print(frame2,'\n')
f= frame1+frame2
print(f,'\n')