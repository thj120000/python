#!@Author : Sanwat
#!@File : .py
'''
SVC方法经过扩展甚至可以用来解决回归问题，这种方法称作支持向量回归（svr)
SVC生成的模型实际上没有使用全部的训练集数据，而是使用其中的一部分，也就是离决策边界最近的数据点。类似的
SVR生成的模型也只是依赖于部分训练数据。
我们将介绍SVR算法是如何使用Diabetes数据集的，本章前面使用过，我们考虑第三个生理数据。我们使用三种不同回归算法：
线性和非线性（多项式）。使用线性内核的SVR算法将生成一条直线作为线性预测模型，非常类似前面见过的线性回归算法，
而使用多项式内核的SVR算法生成二次和三次曲线。


'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

diabetes= datasets.load_diabetes()
x_train= diabetes.data[:-20]
y_train= diabetes.target[:-20]
x_test= diabetes.data[-20:]
y_test= diabetes.target[-20:]

x0_train= x_train[:,2]
x1_train= x0_train[:,np.newaxis]#让索引值返回任然是列向量
x0_test= x_test[:,2]
x1_test= x0_test[:,np.newaxis]

x1_test.sort(axis=0)
x1_test=x1_test*100
x1_train= x1_train*100

svr=svm.SVR(kernel='linear',C=1000)
svr2= svm.SVR(kernel='poly',C=1000,degree=2)
svr3= svm.SVR(kernel='poly',C=1000,degree=3)

svr_train= svr.fit(x1_train,y_train)
svr2_train= svr2.fit(x1_train,y_train)
svr3_train= svr3.fit(x1_train,y_train)

y=svr_train.predict(x1_test)
y2= svr2_train.predict(x1_test)
y3= svr3_train.predict(x1_test)

plt.scatter(x1_test,y_test,color='k')
plt.plot(x1_test,y,color='b')
plt.plot(x1_test,y2,color='r')
plt.plot(x1_test,y3,color='g')
plt.show()
