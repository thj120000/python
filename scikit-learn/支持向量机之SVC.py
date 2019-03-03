#!@Author : Sanwat
#!@File : .py
'''
正则化是一个与SVC算法相关的概念，用参数C来设置：
C值较小，表示计算时间间隔时，将分界线两侧的大量设置全部数据点都考虑在内（泛化能力强）
C值较大，表示只考虑分界线附近的数据点（泛化能力弱）。若不指定C值，默认他的值为1，
我们可以通过support_vector数据获取到参与计算间隔的数据点，为其添加高亮效果。
'''
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
from sklearn import svm

x= np.array(
    [
        [1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],
        [2,1],[3,1],[3,2],[3.5,1],[3.5,3]
    ]
)
y= [0]*6+[1]*5
svc= svm.SVC(kernel='linear',C=1).fit(x,y)
X,Y= np.mgrid[0:4:200j,0:4:200j]
train= svc.decision_function(np.c_[X.ravel(),Y.ravel()])
train=train.reshape(X.shape)
plt.subplot(211)
plt.contourf(X,Y,train>0,alpha=0.4)
plt.contour(X,Y,train,colors=['k','k','k'],linestyles=['--','-','-.'],levels=[-1,0,1])
plt.scatter(svc.support_vectors_[:,0],svc.support_vectors_[:,1],s=120,facecolors='none')
plt.scatter(x[:,0],x[:,1],c=y,s=50,alpha=0.9)
#plt.xlim(x[:,0].min()-0.5,x[:,1].max()+0.5)
#plt.ylim(x[:,1].min()-0.5,x[:,1].max()+0.5)

plt.subplot(212)
svc2= svm.SVC(kernel='linear',C=0.1).fit(x,y)
train2= svc.decision_function(np.c_[X.ravel(),Y.ravel()])
train2= train2.reshape(X.shape)
plt.contourf(X,Y,train2>0,alpha=0.4)
plt.contour(X,Y,train2,colors=['r','r','r'],linestyles=['--','-.','-'],levels=[-1,0,1])
plt.scatter(svc2.support_vectors_[:,0],svc2.support_vectors_[:,1],s=120,facecolors='none')
plt.scatter(x[:,0],x[:,1],c=y,s=50,alpha=0.9)
plt.show()
