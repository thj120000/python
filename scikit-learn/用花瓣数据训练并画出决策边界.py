#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import  ListedColormap
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris= datasets.load_iris()#载入iris数据
x= iris.data[:,2:4]
a= iris.target

x_min,x_max=x[:,0].min()-0.5,x[:,0].max()+0.5
y_min,y_max= x[:,1].min()-0.5,x[:,1].max()+0.5
plt.figure()#打开一张图纸
#布置画布
cmap_light=ListedColormap(['r','b','g'])#画布的颜色
xx,yy=np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))

#k-近邻算法开始训练
knn= KNeighborsClassifier()
train_result= knn.fit(x,a)
'''
ravel将多维数据转换成一维
'''
#预测画布内所有的范围,
predict_result=knn.predict(np.c_[xx.ravel(),yy.ravel()])
#预测结果根据xx.shape来重新划分画布
predict_result=predict_result.reshape(xx.shape)
#将整个画布开始根据训练结果划分区域
plt.pcolormesh(xx,yy,predict_result,cmap=cmap_light)
#将数据点显示在画布上
plt.scatter(x[:,0],x[:,1],c=a)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()