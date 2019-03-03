#!@Author : Sanwat
#!@File : .py
import numpy as np
import datetime #用来设置我们的时间节点
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
'''
定义好两个时间尺度，一个用于日期，一个用于月份。
在xaxis对象上调用set_major_locator函数和set_minor_locator函数，在月份刻度显示上面用set_major_formatter函数
'''

'''
利用datetime来设置我们的时间节点
'''
events= [
    datetime.date(2015,1,23),
    datetime.date(2015,1,28),
    datetime.date(2015,2,3),
    datetime.date(2015,2,21),
    datetime.date(2015,3,15),
    datetime.date(2015,3,24),
    datetime.date(2015,4,8),
    datetime.date(2015,4,24)
]
readings= [12,22,25,20,19,15,17,14]
moths= mdates.MonthLocator()#获取本地的设置月份
days= mdates.DayLocator()#获取本地的设置日
timeFmt= mdates.DateFormatter('%Y-%m')#获取本地的设置格式
fig, ax= plt.subplots()
plt.plot(events,readings)
'''
为X轴设置两种不同的标签
'''
ax.xaxis.set_major_locator(moths)#横坐标显示的最大间隔
ax.xaxis.set_minor_locator(days)#横坐标显示的最小间隔
'''
月标签的刻度显示
'''
ax.xaxis.set_major_formatter(timeFmt)#横坐标的设置格式
plt.show()