#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
bar()类型，可以将pandas 的dataframe he series用图表表示出来 
'''
plt.figure(1)
series1= np.array([3,4,5,3])
series2= np.array([1,2,2,5])
series3= np.array([2,3,3,4])
index= np.arange(4)
plt.axis([0,4,0,15])
plt.bar(index,series1,color='r')
plt.bar(index,series2,color='g',bottom=series1)
plt.bar(index,series3,color='b',bottom=series1+series2)
plt.xticks(index-0.4,['Jan15','Feb15','Mar15','Apr15'])
plt.show()

plt.figure(2)
plt.axis([0,15,0,4])
plt.barh(index,series1,color='g')
plt.barh(index,series2,color='r',left=series1)
plt.barh(index,series3,color='b',left=series1+series2)
plt.yticks(index-0.4,['Jan','Feb','Mar','Apr'])
plt.show()

'''
下面我们用不同的颜色来区分多个序列。
'''
plt.figure(3)
plt.axis([0,15,0,4])
plt.title('A Multiseries Horizontal Bar Chart',fontsize=20,color='r')
plt.barh(index,series1,color='w',hatch='xx')#hatch关键字指定线条的类型
plt.barh(index,series2,color='w',hatch= '///',left=series1)
plt.barh(index,series3,color='w',hatch='\\\\\\',left=series1+series2)
plt.yticks(index-0.4,['Jan','Feb','Mar','Apr'])
plt.show()

