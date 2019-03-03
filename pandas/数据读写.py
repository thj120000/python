#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
'''
read_csv  ; to_csv
read_excel  ;to_excel
read_hdf  ; to_hdf
read_sql  ; to_sql
read_html  ;to_html
read_stata  ;to_stata
read_pickle  ;to_pickle
带实验性质
read_msgpack  ；to_msgpack
read_gbq  ;to_gpq
'''
'''
读取csv或文本中的数据
'''
csvframe= pd.read_csv('mycsv_01.csv')
print (csvframe,'\n')
csvframe2= pd.read_table('mycsv_01.csv',sep=',')
print(csvframe2,'\n')

csvframe3= pd.read_csv('mycsv_02.csv')
print (csvframe3,'\n')
#添加表头

csvframe4= pd.read_csv('mycsv_02.csv',header= None)
print (csvframe4,'\n')
