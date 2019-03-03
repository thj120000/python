#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import html5lib

from pandas.io.json import json_normalize

'''
JSON对象标记，
'''
frame= pd.DataFrame(
    np.arange(16).reshape(4,4),
    index=['white','black','red','blue'],
    columns=['up','down','right','left']
)
print (frame,'\n')
#写入json数据，即将dataframe对象转换成json
json1= frame.to_json('frame.json')
'''
逆操作，读取json文件，利用read_json()函数
'''
rdjson= pd.read_json('frame.json')
print (rdjson,'\n')

'''
然而通常下，json文件中的数据通常不是列表形式，因此需要将字典结构的文件转换成列表形式，即规范化。
pandas 中的json_normalize()函数能够将字典或列表转换为表格。
'''

file= open('books.json.txt','r')
text = file.read()
text = pd.io.json.loads(text)
rdjson2= json_normalize(text,'books')
print (rdjson2,'\n')
