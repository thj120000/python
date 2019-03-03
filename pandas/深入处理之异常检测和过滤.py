#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

randframe= pd.DataFrame(
    np.random.randn(1000,3)
)
print (randframe,'\n')
describe= randframe.describe()#查看每一列的描述性统计量。均值/标准差等等
print (describe,'\n')
#单独查看统计量，如标准差
std= randframe.std()
print (std,'\n')
#平均值
mean= randframe.mean()
print (mean ,'\n')
'''
根据每一列的标准差，对dataframe 的所有对象元素进行过滤。借助any()函数，进行筛选
下面就是将比标准差大三倍的元素作为异常值筛选出来。
'''
shaixuan= randframe[(np.abs(randframe)>(3*randframe.std())).any(1)]
print(shaixuan,'\n')