#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd



mydict = {'red':2000,'blue':1000,'yellow':500,'orange':1000}
myseries= pd.Series(mydict)
mydict2 = {'red':400, 'yellow':1000,'black':700}
myseries2= pd.Series(mydict2)
s= myseries+myseries2
print (s,'\n')