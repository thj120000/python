#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import html5lib

'''
read_html(),to_html(),这两个函数非常有用，可以把复杂的数据结构转换成html表格，如果从事web开发，则很方便
to_html()函数可以直接把DataFrame转换成HTML表格
'''
frame = pd.DataFrame(np.arange(4).reshape(2,2))
print (frame,'\n')
html1= frame.to_html()
print (html1,'\n')
'''
frame= pd.DataFrame(
    np.random.random((4,4)),
    index=["white",'black','red','blue'],
    columns=['up','down','right','left']
)
print (frame,'\n')


创建一个包含HTML的页面代码的字符串
'''
s=['<HTML>']
s.append('<HEAD><TITLE>my dataframe</TITLE><HEAD>')
s.append('<BODY>')
s.append(frame.to_html())
s.append('<BODY></HTML>')
html= ''.join(s)

'''
把html写入到myframe.html文件中
'''
html_file= open('myframe.html','w')
html_file.write(html1)
html_file.close()
'''
把html2写入到myframe2.html文件中

html_file= open ('myframe.html2','w')
html_file.write(html)
html_file.close()
'''

