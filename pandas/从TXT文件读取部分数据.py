#!@Author : Sanwat
#!@File : .py
import numpy as py
import pandas as pd

'''
假如你只想读取文件的部分数据，可以明确指定要解析的行号，这时要用到nrows 和skiprows ,你可以指定起始行
（n= skiprows ) 和 从起始行往后读多少行（nrows= i). 
'''
lizi= pd.read_csv('mycsv_02.csv',skiprows=[2],nrows= 4,header=None)
#跳过第三行，从头开始读，读四行
print(lizi,'\n')
'''
切分想要解析的文本，然后遍历各个部分，逐一对其执行某一特定操作。
例子：对于一列数字，每隔两行取一个累加起来，最后把和插入到Series对象中。
'''
out = pd.Series()
i= 0
pieces= pd.read_csv('mycsv_01.csv',chunksize=5)#执行五次，即前五行求和
for piece in pieces:
    out.set_value(i,piece['white'].sum())
    i=i+1
#print(i,'\n')
print (out,'\n')


