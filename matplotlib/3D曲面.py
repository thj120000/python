#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  mpl_toolkits.mplot3d  import  Axes3D

fig= plt.figure(1)
ax= Axes3D(fig)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(X,Y)
def f(x,y):
    return (1-y**5+x**5)*np.exp(-x**2-y**2)
ax.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1)
plt.show()

fig2=plt.figure(2)
ax2=Axes3D(fig2)
X=np.arange(-2,2,0.1)
Y=np.arange(-2,2,0.1)
X,Y=np.meshgrid(X,Y)
ax2.plot_surface(X,Y,f(X,Y),rstride=1,cstride=1,cmap=plt.cm.hot)
'''
elev关键字：表示指定从哪一个高度查看曲面，
azim关键字：表示指定从哪一个旋转的角度查看曲面
'''
ax2.view_init(elev=30,azim=125)
plt.show()