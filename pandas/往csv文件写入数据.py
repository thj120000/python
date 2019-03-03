#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

frame2= pd.DataFrame(
    np.arange(12).reshape((3,4)),
    columns= ['blue','green','white','yellow']

)
print (frame2,'\n')
save1= frame2.to_csv('save1.csv')
'''
去掉标题，索引
'''
save2= frame2.to_csv('save2.csv',index= False)