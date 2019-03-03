#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

'''
to_excel()
read_excel()函数能够读取excel2003(.xls)和excel2007(.xlsx)两种类型的文件。因为该函数整合了xlrd模块
'''
'''
新建一个excel 表格，保存为data.xls
'''
excel= pd.read_excel('data.xlsx')
print(excel,'\n')

excel2= pd.read_excel('data.xlsx','Sheet2')
print (excel2,'\n')

'''
也可以将一个dataframe对象转换成excel

'''
frame= pd.DataFrame(
    np.random.random((4,4)),
    index=['exp1','exp2','exp3','exp4'],
    columns=['Jan','Feb','Mar','Apr']
)
print (frame,'\n')
frame.to_excel('data2.xlsx')
