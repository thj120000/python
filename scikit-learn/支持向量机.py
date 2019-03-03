#!@Author : Sanwat
#!@File : .py
'''
支持向量机(SVM)
SVM分类器是二元或判别模型，对两类数据进行区分。它的基础任务是判断新观测数据属于两个类别中的哪一个。在学习阶段，这类分类把
训练数据映射到叫做决策空间的多维空间，创建叫做决策边界的分里面，把决策空间分为两个区域。在最简单的线性可分的情况下，决策边界
可以用平面3D或者直线2D表示。在更复杂的情况中，分离面为曲面，形状更为复杂
SVM算法既可以用于回归问题。比如（SVR:支持向量回归)
也可以用于分类，比如（SVC:支持向量分类）
'''

'''
1,支持向量分类-1
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import linear_model
from sklearn import kernel_approximation
from sklearn import  svm

x=np.array([
    [1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],
    [2,1],[3,1],[3,2],[3.5,1],[3.5,3]
])
print ('数据集：',x,'\n')
y= [0]*6+[1]*5
'''
用训练集训练SVC算法之前，先用SVC()构造函数定义模型，我们使用线性内核（内核指的是用于模式分析的一类算法）
然后调用fit()函数，传入训练集作为参数。模型训练完成后用decision_funtion ()函数绘制决策边界。
'''
svc= svm.SVC(kernel='linear').fit(x,y)
#设置决策画布
X,Y=np.mgrid[0:400:200j,0:400:200j]
train =svc.decision_function(np.c_[X.ravel(),Y.ravel()])
train =train.reshape(X.shape)
plt.contourf(X,Y,train>0,alpha=0.4)
plt.contour(X,Y,train,colors=['k'],linestyles= ['-'],levels=[0])
plt.scatter(x[:,0],x[:,1],c=y,s=50,alpha=0.9)#alpha透明度
plt.xlim(x[:,0].min()-0.5,x[:,0].max()+0.5)#设置横坐标显示范围
plt.ylim(x[:,1].min()-0.5,x[:,1].max()+0.5)#设置纵坐标显示的范围
plt.show()