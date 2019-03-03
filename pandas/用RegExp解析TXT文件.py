#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

'''
元字符
.   换行符以外的单个字符
\d  数字
\D  非数字字符
\s  空白字符
\S  非空白字符
\n  换行符
\t  指标符
\ uxxxx  用十六进制数表述xxxx的Unidode字符

'''

ch_01= pd.read_table('ch01.txt',sep= '\s*')
print (ch_01,'\n')
ch_02= pd.read_table('ch02.txt',sep= '\D*',header= None)
print(ch_02,'\n')
'''
使用skiprows 选项排除多余的行，skiprows= 5即排除前五行，skiprows =[5]即排除第五行
'''
ch_03= pd.read_table('ch03.txt',sep=',',skiprows=[0,1,3,6])
print (ch_03,'\n')
