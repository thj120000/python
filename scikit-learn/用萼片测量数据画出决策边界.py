#!@Author : Sanwat
#!@File : .py

from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import  ListedColormap  #决策边界函数
import numpy as np
from sklearn import datasets
'''
将上述结果绘制的2D散点图中，画出决策边界
'''
iris= datasets.load_iris()
x2=iris.data[:,:2]#所有行，第一列和第二列所有的值,即萼片的值
a=iris.target

x2_min,x2_max= x2[:,0].min()-0.5, x2[:,0].max()+0.5
y2_min,y2_max= x2[:,1].min()-0.5, x2[:,1].max()+0.5
#MESH
cmap_light= ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h=0.02
xx,yy= np.meshgrid(np.arange(x2_min,x2_max,h),np.arange(y2_min,y2_max,h))#设置图形的范围区域
knn=KNeighborsClassifier()#调用k-近邻算法
train_result=knn.fit(x2,a)#调用近邻算法的fit()函数进行训练
'''
接下来预测，预测值乃是未知值
'''
Z=knn.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
plt.figure(1)
plt.scatter(x2[:,0],x2[:,1],c=a)#用三种颜色标出前两行的数据（即萼片），横坐标为第一列的值，纵坐标为第二列的值
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("the data of sepal")
plt.show()

plt.figure(2)
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)#为整幅图划分三个颜色区域，划分依据：xx,yy,z。即预测结果
#标出训练点
plt.scatter(x2[:,0],x2[:,1],c=a)#用三种颜色标出前两行的数据（即萼片），横坐标为第一列的值，纵坐标为第二列的值
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.title("the data of sepal's training result")
plt.show()