#!@Author : Sanwat
#!@File : .py
'''
前面用过的SVC算法从仅包含两个类别的训练集中学习。接下俩测试iris 数据集，共有三中花卉
对于这个数据集，决策边界相互交叉，把决策空间（2D）或者决策体（3D)分成多个部分。
两个线性模型均有线性决策边界（相交的超平面），而使用的非线性内核的模型（多项式或高斯RBF）有非线性决策边界，
后者在处理依赖于内核和参数的数据时更为灵活。
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris= datasets.load_iris()
x= iris.data[:,:2]#前两列
y= iris.target #鸢尾花的三个种类
h=0.05
svc= svm.SVC(kernel='linear',C=1).fit(x,y)
x_min,x_max=x[:,0].min()-0.5, x[:,0].max()+0.5
y_min, y_max= x[:,1].min()-0.5, x[:,1].max()+0.5

plt.figure(1)
plt.subplot(121)
X,Y= np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))

train= svc.predict(np.c_[X.ravel(),Y.ravel()])
train= train.reshape(X.shape)

plt.contourf(X,Y,train,alpha=0.4)
plt.contour(X,Y,train,colors='r')

plt.scatter(x[:,0],x[:,1],c=y)

plt.subplot(122)
svc2= svm.SVC(kernel='poly',C=1,degree=3).fit(x,y)
X,Y= np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
train2= svc2.predict(np.c_[X.ravel(),Y.ravel()])
train2= train2.reshape(X.shape)
plt.contourf(X,Y,train2,alpha=0.4)
plt.contour(X,Y,train2,colors='r')
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()

plt.figure(2)
svc3= svm.SVC(kernel='rbf',C=1,gamma=3).fit(x,y)
train3= svc3.predict(np.c_[X.ravel(),Y.ravel()])
train3= train3.reshape(X.shape)
plt.contourf(X,Y,train3,alpha=0.4)
plt.contour(X,Y,train3,colors='r')
plt.scatter(x[:,0],x[:,1],c=y)
plt.show()