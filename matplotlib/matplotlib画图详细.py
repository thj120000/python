#!@Author : Sanwat
#!@File : .py


import numpy as np
import matplotlib.pyplot as plt
#line
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
#定义余弦函数正弦函数
c,s=np.cos(x),np.sin(x)
plt.figure(1)
#画图，以x为横坐标，以c为纵坐标
plt.plot(x,c,color="blue",linestyle="-",label="COS",alpha=0.5)
plt.plot(x,s,"r*",label="SIN")
#增加标题
plt.title("COS & SIN")
ax=plt.gca()
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
plt.yticks(np.linspace(-1,1,5,endpoint=True))
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))
#图例显示
plt.legend(loc="upper left")
#显示网格
plt.grid()
#显示范围
#plt.axis([-1,1,-0.5,1])
plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color="green",alpha=0.25)
t=1
plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),
textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
#显示图形
plt.show()