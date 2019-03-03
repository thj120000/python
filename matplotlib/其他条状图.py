#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x= np.arange(8)
y1= np.array([1,3,4,6,4,3,2,1])
y2= np.array([1,2,5,4,3,3,2,1])
plt.ylim(-7,7)#设置纵坐标的显示范围
plt.bar(x,y1,0.9,facecolor='r',edgecolor='w')
plt.bar(x,-y2,0.9,facecolor='r',edgecolor='w')
plt.xticks(())
plt.grid(True)#显示网格
'''
利用for循环显示和text函数显示y值的标签
'''
for a,b in zip(x,y1):
    plt.text(a,b+0.05,'%d'%b,ha='center',va='bottom')
for a,b in zip(x,y2):
    plt.text(a,-b-0.5,'%d'%b,ha='center',va='bottom')
plt.show()