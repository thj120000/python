#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import html5lib
'''
1，创建一个数据库dataframe对象
'''
frame= pd.DataFrame(
    np.random.random((4,4)),
    index=["white",'black','red','blue'],
    columns=['up','down','right','left']
)
print (frame,'\n')
#将dataframe转换成html
print (frame.to_html())
'''
2,创建一个包含html页面代码的字符串
'''
a=['<HTML>']
a.append('<HEAD><TITLE>my dataframe</TITLE><HEAD>')
a.append('<BODY>')
a.append(frame.to_html())
a.append('<BODY></HTML>')
html= ''.join(a)
'''
3,HTML页面的所有内容都存储再变量html中，接下来把它写入到myframe2.html中，那么工作目录会多了myframe2.html文件，双击可以用浏览器打开
'''
html_file= open ('myframe2.html','w')
html_file.write(html)
html_file.close()