#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
import math
'''
1,添加文本
'''
plt.figure(1)
plt.axis([0,5,0,20])#设置横纵坐标的范围
plt.title('My second plot',fontsize=20,fontname= 'Times New Roman',color= 'red')#设置标题的颜色，字体，大小和内容
plt.xlabel('Counting',color= 'blue')#设置横坐标的名称和颜色
plt.ylabel('Square values',color='green')
'''
在图表的任意位置添加文本
text(x,y,s,fontdict=None, **kwargs)
前两个参数为文本在图形中位置的坐标。s为要添加的字符串，fontdict 是文本要用的字体
'''
plt.text(1,1.5,'First',color= 'green')
plt.text(2,4.5,'Second',color='red')
plt.text(3,9.5,'Third',color='blue')
plt.text(4,16.5,'Forth',color= 'black')
'''
2,将表达式内容置于两个$符号之间，可以在文本中添加LaTex表达式。解释器会将他转换成公式数学符号之类
不过，前面要加上r字符，表明它后面是原始文本，不能进行转义操作
'''
plt.text(1.1,10.8,r'$y=x^2$',fontsize= 20,bbox={'facecolor':'yellow','alpha':0.2})
'''
3,添加网格
'''
plt.grid(True)
'''
4,添加图例
legend ()可以将图例和字符串类型的图例说明添加到图表中
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro')#设置坐标点
plt.plot([1,2,3,4],[0.9,3.5,8,15],'g+')
plt.plot([1,2,3,4],[0.5,3,7,13],'b*')
plt.legend(['First series','Second series','Third series'],loc=2)
plt.savefig('my_chart.png')#保存图表
'''
图列的位置（loc=)关键字
0   最佳位置
1   右上角
2   左上角
3   右下角
4   左下角
5   右侧
6   左侧垂直居中
7   右侧垂直居中
8   下方水平居中
9   上方水平居中
10  正中间
'''
plt.show()
'''
5,保存图片
'''


