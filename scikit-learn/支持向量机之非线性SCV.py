#!@Author : Sanwat
#!@File : .py
'''
你已经见识过SVC线性算法，它旨在定义一条把数据分为两类的分界线。还有有些更为复杂的SVC算法，它们能够建立曲线（2D)或曲面(3D),
所依据的原则依然是最大化离表面最近的数据点之间的距离。
例如，我们定义一个多项式内核的系统，我们定义一条多项式曲线把决策空间分为两块。多项式的次数可用degree选项指定。即使是非线性SVC
，C依旧是正则化回归系数。我们尝试使用内核为三次多项式/回归系数C取1的SVC算法。

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from sklearn import linear_model
from sklearn import  datasets
from sklearn.neighbors import KNeighborsClassifier

x=np.array(
    [
        [1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],
        [2,1],[3,1],[3,2],[3.5,1],[3.5,3]
    ]
)
y= [0]*6+[1]*5
plt.figure(1)
#利用kernel选择非线性svc分析,linear表示线性分析，poly表示曲线分析
svc= svm.SVC(kernel='poly',C=1,degree=3).fit(x,y)
X,Y= np.mgrid[0:4:200j,0:4:200j]
train= svc.decision_function(np.c_[X.ravel(),Y.ravel()])
train=train.reshape(X.shape)
plt.contourf(X,Y,train>0,alpha=0.4)
plt.contour(X,Y,train,colors=['r','g','b'],linestyles=['--','-','-.'],levels=[-1,0,1])
plt.scatter(svc.support_vectors_[:,0],svc.support_vectors_[:,1],s=120,facecolors= 'none',color='k')
plt.scatter(x[:,0],x[:,1],c=y,s=50,alpha=0.9)
plt.show()
'''
另一种非线性内核为径向基函数（radial basis function,rbf) 。设置关键字参数gamma。
这种内核生成的分隔面尝试把数据集的各个数据点分到沿径向方向分布的不同区域。
'''
plt.figure(2)
svc2= svm.SVC(kernel='rbf',C=1, gamma=3).fit(x,y)
train= svc2.decision_function(np.c_[X.ravel(),Y.ravel()])
X,Y= np.mgrid[0:4:200j,0:4:200j]
train= train.reshape(X.shape)
plt.contourf(X,Y,train>0,alpha= 0.4)
plt.contour(X,Y,train,colors=['r','k','b'],linestyles= ['-','-.','--'],levels= [-1,0,1])
plt.scatter(svc2.support_vectors_[:,0],svc2.support_vectors_[:,1],s=120,facecolors='none',color='k')
plt.scatter(x[:,0],x[:,1],c=y,s=50,alpha=0.9)
plt.show()