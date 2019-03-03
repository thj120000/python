#!@Author : Sanwat
#!@File : .py
'''
近邻分类器是最简单的分类器。近邻算法搜索训练集，寻找与用作测试的新个体最相似的观测记录
训练集：专门用于训练算法
测试集：专门用于验证算法

接下来还是用鸢尾花的数据集，我们用numpy.random.permutation()打乱数据集的所有元素。然后用140条作为训练集，剩余10条作为测试集
'''

import matplotlib.pyplot as plt
from matplotlib.colors import  ListedColormap  #决策边界函数
import numpy as np
from sklearn import datasets
np.random.seed(0)#用于固定我们随机打算后的顺序
iris= datasets.load_iris()
x= iris.data#所有的数据
y= iris.target#鸢尾花的类别
i=np.random.permutation(len(iris.data))
x_train= x[i[:-10]]#从0-140个数据
y_train= y[i[:-10]]#从0-140个数据
print("x_train训练集：",x_train,'\n')
print("y_train训练集：",y_train,'\n')
x_text= x[i[-10:]]#从140-150个数据
y_text= y[i[-10:]]#从140-150个数据
print ("y_text实际值：",y_text,'\n')
'''
开始 K-近邻算法
导入k-neighborsClassifier ,调用分类器的构造函数，然后用fit()函数对其进行训练
'''

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier()
#将训练结果显示出来
train_result=knn.fit(x_train,y_train)
print (train_result,'\n')
'''
我们用140条观测数据训练knn分类器得到了预测模型。接下来验证他的效果。
分类器应该能够正确预测测试集中10条观测数据所对应的类别。可以在预测模型knn上调用predict（）函数。
'''
predict_result=knn.predict(x_text)#根据knn的训练结果类比，利用140-150的十个数，预测得出的结果
print("根据训练得出的预测结果：",predict_result,'\n')
print('原始的数据集：',y_text,'\n')


