#!@Author : Sanwat
#!@File : .py

import pandas as pd
import csv
import html5lib


'''
read_html()函数借些html页面，寻找html表格，如果找到，则会返回一个dataframe列表。
例如，下面的网址所指向的页面的html表格为一个排行榜，包含用户的名字和得分两行。如果索引只有一个元素，那么索引为0

pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False, tupleize_cols=None, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)

常用的参数：
io:可以是url、html文本、本地文件等；
flavor：解析器；
header：标题行；
skiprows：跳过的行；
attrs：属性，比如 attrs = {'id': 'table'}；
parse_dates：解析日期

注意：返回的结果是**DataFrame**组成的**list**。
'''
rank= pd.read_html('http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/')
print (rank,'\n')


web_frame = pd.read_html('myframe2.html')
print (web_frame,'\n')

'''
例子2：抓取网页的数据，并保存到csv文件中
'''
for i in range(1,178):  # 爬取全部177页数据
	url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
	tb = pd.read_html(url)[3] #经观察发现所需表格是网页中第4个表格，故为[3]
	tb.to_csv(r'抓取1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
	print('第'+str(i)+'页抓取完成')
