#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
text= '16 Bottle Avenue , Boston'
text1= text.split(',')#利用split()函数对字符串进行分隔
print (text1,'\n')
'''
strip()去掉空格
'''

token= [s.strip() for s in text.split(',')]
print (token,'\n')

'''
还可以利用以下进行赋值
'''
name1,name2=[s.strip() for s in text.split(',')]
print (name1,'\n')
print (name2,'\n')

'''
文本连接
'''
str1= name1+','+name2
print(str1)
strings= ['A+','A','A-','B+','B','B-','CCC','C+']
str2= ';'.join(strings)
print (str2)
'''
字符串查找index（），find()
'''
find1= text.index('Boston')
find2= text.find('Boston')
print (find1,find2)#这两个查找到的结果都是字符串中的索引。
'''
想要查看字符串中字母出现的次数，利用count（）函数
'''
e= text.count('e')
print ('字母e出现的次数：',e,'\n')

'''
删除或者替换字符串
'''
tihuan= text.replace('Avenue','Street')
print (tihuan,'\n')
shanchu= text.replace('1','')#用空字符代替字符串，效果等同于删除
print (shanchu,'\n')