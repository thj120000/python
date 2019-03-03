#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dx=0.01
dy=0.01
x= np.arange(-2,2,dx)
y= np.arange(-2,2,dy)
X,Y= np.meshgrid(x,y)
plt.figure(1)
'''
定义一个函数计算f（x,y）,用contour（)生成三维结构表面的等值线图
'''
def f(x,y):
    return (1-y**5+x**5)*np.exp(-x**2-y**2)
C=plt.contour(X,Y,f(X,Y),8,colors='black')
plt.contourf(X,Y,f(X,Y),8)
'''
clable()等值线图参数传递
'''
plt.clabel(C,inline=1, fontsize=10)
plt.show()
plt.figure(2)
C=plt.contour(X,Y,f(X,Y),8,colors='black')
plt.contourf(X,Y,f(X,Y),8,cmap=plt.cm.hot)
'''
*在图像的右侧加上图列,利用colorbar()函数
'''
plt.clabel(C,inline= 1, fontsize=10,color= 'black')
plt.colorbar()
plt.show()