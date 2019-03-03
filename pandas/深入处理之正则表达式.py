#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import re

'''
表示一个或者多个空白符的正则表达式为\s+
'''
text= 'This is    an\t odd \n text!'
text1= re.split('\s+',text)
print (text1,'\n')

regex= re.compile('\s+')
print (regex,'\n')
text= regex.split(text)
print (text,'\n')
'''
findall () 函数可匹配 文本中所有符合正则表达式的子串。该函数返回一个列表，元素为文本中所有符合正则表达式的字串
'''
text3= 'This is my address: 16 Botton Avenue, Boston'
text4= re.findall('A\w+',text3)#找出以A打头的字符串
print (text4,'\n')
text5= re.findall('B\w+',text3)#找出以B打头的字符串
print (text5,'\n')
text6= re.findall('[A,a]\w+',text3)
print (text6,'\n')
'''
search()仅返回第一处符合模式的子串,并且返回对象为一个特殊类型的对象
'''
text7=re.search('A\w+',text3)
print(text7,'\n')
text8=re.search('[A,a]\w+',text3)#仅返回了第一处的字符串
print (text8,'\n')
text9= text3[text8.start():text8.end()]
print (text9,'\n')

'''
match()函数从字符串开头开始匹配，如果第一个不同，则不会返回值
'''
text10= re.match('[A,a]\w+',text3)
print (text10,'\n')
text11= re.match('T\w+',text3)
print (text11,'\n')

