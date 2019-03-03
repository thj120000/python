#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd


#利用name指定表头
csvframe6= pd.read_csv('mycsv_02.csv',names= ['white','red','blue','green','animal'])
print (csvframe6,'\n')


#新建的csv文件其中有两行用作等级索引

csvframe5= pd.read_csv('mycsv_03.csv',index_col=['color','status'])
print(csvframe5,'\n')
