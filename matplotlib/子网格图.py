#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
gridspec将画布分为3*3个
'''
gs= plt.GridSpec(3,3)
fig= plt.figure(figsize=(6,6))
x1= np.array([1,3,2,5])
y1= np.array([4,3,7,2])
x2= np.arange(5)
y2= np.array([3,2,4,6,4])

s1= fig.add_subplot(gs[1,:2])#第二行第一个图，表示第二行，从0到第二个之前
s1.plot(x2,y2,'r')#折线
s2= fig.add_subplot(gs[0,:2])#第一行第一个，表示第一行，从0到第二个之前
s2.bar(x2,x2,color='g')#条形图
s3= fig.add_subplot(gs[2,0])#第三行第一个,并且是方形图，表示第三行，第一个
s3.barh(x2,y2,color='purple')
s4= fig.add_subplot(gs[:2,2])#第一行最右边的那个，表示第二行以前，第三列
s4.plot(x2,y2,'k')
s5= fig.add_subplot(gs[2,1:])#表示第三行，第一个开始以后的区域
s5.plot(x1,y1,'ro',x2,y2,'b*')

plt.show()