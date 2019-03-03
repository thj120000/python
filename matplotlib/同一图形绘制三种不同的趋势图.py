#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
import math
'''
t= np.arange(0,2.5,0.1)
y1= map(math.sin, math.pi*t)

y2= map(math.sin , math.pi*t+math.pi/2)
y3= map(math.sin, math.pi*t-math.pi/2)
plt.plot(t,y1,'ro')#,'b*',t,y2,'g^',t,y3,'ys')
plt.show()
'''
#line
x=np.linspace(-math.pi,math.pi,512,endpoint=True)
#定义余弦函数正弦函数
c,s=np.cos(x),np.sin(x)

plt.figure(1)
#画图，以x为横坐标，以c为纵坐标
plt.plot(x,c,color="blue",linestyle="-",label="COS",alpha=0.5)
plt.plot(x,s,"r*",label="SIN")
#增加标题
plt.title("COS & SIN")
plt.show()


t= np.arange(-np.pi,np.pi,0.1)
y1= np.sin(t)
y2= np.sin(t-np.pi/2)
y3= np.sin(t+np.pi/2)
plt.figure(2)
plt.plot(t,y1,'b*',t,y2,'r*',t,y3,'g*')
plt.show()