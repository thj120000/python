#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd


'''
HDF5库关注的是HDF5 的读写，这种文件的数据结构由节点组成，能够存储大量数据集
'''

from pandas.io.pytables import HDFStore

frame= pd.DataFrame(
    np.arange(16).reshape(4,4),
    index=['white','black','red','blue'],
    columns=['up','down','right','left']
)
print (frame,'\n')

store= HDFStore('mydata.h5')
store['obj1']= frame
print (store,'\n')