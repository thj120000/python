#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

frame= pd.DataFrame(
    {
        'item':['ball','mug','pen','pencil','ashtray'],
        'color':['white','rosso','verde','black','yellow'],
        'price':[5.56,4.20,1.30,0.56,2.75]
    }
)
print (frame,'\n')

bins=[0,25,50,75,100]
cat= pd.cut(,bins)
print(cat,'\n')