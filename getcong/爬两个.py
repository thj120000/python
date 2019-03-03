#!@Author : Sanwat
#!@File : .py
# -*- coding :utf-8 -*-

import requests
from lxml import etree
import matplotlib.pyplot as plt
import time #导入时间模块，以免豆瓣封你IP

url = "https://movie.douban.com/subject/26942674/?from=showing"
data = requests.get(url).text
s= etree.HTML(data)
#给定url 并用requests.get()方法来获取页面的text, 用etree.HTML()
#来解析下载的页面数据“data"

#s.xpath = ('元素的xpath 信息/text()')
film_name = s.xpath ('//*[@id="content"]/h1/span[1]/text()')
director= s.xpath ('//*[@id="info"]/span[3]/span[2]/a/text()')
picture= s.xpath('//*[@id="mainpic"]/a/img')


#由于导演有时候不止一个人，所以我这里以列表的形式输出
ds = []
for d in director:
    ds.append(d)

print ("电影名：", film_name)
print ("主演：", ds)
print("图片：",picture)
plt.show(picture)


