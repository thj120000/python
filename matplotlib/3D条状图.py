#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x= np.arange(8)
y= np.random.randint(0,10,8)
y2= y+np.random.randint(0,3,8)
y3= y2+np.random.randint(0,3,8)
y4= y3+np.random.randint(0,3,8)
y5= y4+np.random.randint(0,3,8)
col=['red','blue','yellow','green','black','grey','pink','purple']
fig= plt.figure()
ax= Axes3D(fig)
ax.bar(x,y,0,zdir='y',color=col)
ax.bar(x,y2,10,zdir='y',color=col)
ax.bar(x,y3,20,zdir='y',color=col)
ax.bar(x,y4,30,zdir='y',color=col)
ax.bar(x,y5,40,zdir='y',color=col)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.view_init(elev=40)
plt.show()