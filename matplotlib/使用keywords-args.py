#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
import math

#picture1= plt.plot([1,2,34,2,1,0,1,2,14],linewidth= 2.0)#linewidth改变线条的粗细
#plt.show()
'''
处理多个figure 和Axes对象
subplot()函数可以设置分区模式和当前子图。
他的参数由三个整数组成，第一个数字决定图形沿垂直方向被分为几个部分，第二个数字决定图形沿水平方向被分为几个部分，第三个数字设定直接命令控制的子图
'''
t=np.arange(0,5,0.01)
y1= np.sin(2*np.pi*t)
y2= np.sin(2*np.pi*t)
plt.figure(1)
plt.subplot(211)
plt.plot(t,y1,'b-')
plt.subplot(212)
plt.plot(t,y2,'r*')
plt.show()
'''
把图象分为左右两个子图
'''
plt.figure(2)
plt.subplot(121)
plt.plot(t,y1,'g.')
plt.subplot(122)
plt.plot(t,y2,'b+')
plt.show()
