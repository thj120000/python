#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
颜色编码
b   蓝色
g   绿色
r   红色
c   蓝绿色
m   洋红色
y   黄色
k   黑色
w   白色
'''
x= np.arange(-2*np.pi,2*np.pi,0.01)
y= np.sin(3*x)/x
y2= np.sin(2*x)/x
y3= np.sin(x)/x

plt.plot(x,y,'-.',color= 'red',linewidth= 2)
plt.plot(x,y2,'--',color='blue',linewidth=2)
plt.plot(x,y3,color= 'green',linewidth=2)
'''
xticks() ,yticks()为两列坐标传入数值
'''
plt.xticks(
    [-2*np.pi,-np.pi,0,np.pi,2*np.pi],
    [r'$-2\pi$',r'$-\pi$',r'$0$',r'$\pi$',r'$2\pi$']
)
plt.yticks(
    [-1,0,1,2,3],
    [r'$-1$',r'$0$',r'$1$',r'$2$',r'$3$']
)

'''
笛卡尔坐标系，使得坐标位于图像中间
首先用gca()函数获取axes 图像，该函数可以指定每条边的位置：右，左，上，下。使用set_color 把颜色设置为none。
然后用set_position()移动跟x,y轴相符的边框，使其穿过原点
'''
ax= plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#获取底线
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')#获取左线
ax.spines['left'].set_position(('data',0))
plt.savefig('my_chart2.jpg')
plt.show()


