#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
'''
pandas 序列化并不是完全使用ASCII编码,总的来说，利用pickle可以把粗数据藏起来，使别人看不懂，只有自己可以读取
'''

frame= pd.DataFrame(
    np.arange(16).reshape(4,4),
    index=['up','down','left','right']
)
print (frame,'\n')
#工作目录将生成新文件frame.pkl文件，其包含frame 中的所有信息
pkl1= frame.to_pickle('frame.pkl')
#使用以下命令，将可以打开pkl文件，读取里面的内容
rdpkl= pd.read_pickle('frame.pkl')
print (rdpkl,'\n')
