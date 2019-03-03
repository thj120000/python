#!@Author : Sanwat
#!@File : .py
'''
本章面对的问题看作读取和解释手写体数字图像，预测图像之中的数值。
这类数据分析问题，需要用到估计器（estimator)。它借助fit()函数进行学习，待自己的预测能力到达一定水准后，再用predict()函数
给出预测结果，拿到结果后，我们还会讨论训练集和验证集。
与之前不同的是，这两个数据集是由一系列图像组成的。

我把代码写到这里面，到时候再复制在Ipython notebook中运行即可。
'''

from sklearn import datasets
digits=datasets.load_digits()
print (digits.DESCR)
'''
手写体数字图像的数据，存储在digits.images 数组中。数组的每一个元素表示一张图像，每个元素为8*8形状的矩阵，
矩阵各项为数值类型，每个数值对应一种灰度等级，其中0对应白色，15对应黑色。
'''
print (digits.images[0],'\n')

import matplotlib.pyplot as plt
#%matplotlib inline
plt.figure(1)
plt.imshow(digits.images[0],cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

'''
图像所表示的数字，也就是目标值，则存储在digits.target数组中
'''
print(digits.target,'\n')
'''
据说该数据集有1797张图像，我们可以确认一下
'''
print(digits.target.size,'\n')

'''
接下来，我们进行学习和预测。
digits数据由1797个元素组成，可以考虑用前1791个作为训练集，用剩余的6个作为验证集。
我们可再次用matplotlib 生成这六个手写数字的图像，以便查看其细节
'''
plt.figure(2)
plt.subplot(321)
plt.imshow(digits.images[1791],cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(322)
plt.imshow(digits.images[1792],cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(323)
plt.imshow(digits.images[1793],cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(324)
plt.imshow(digits.images[1794],cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(325)
plt.imshow(digits.images[1795],cmap=plt.cm.gray_r, interpolation='nearest')
plt.subplot(326)
plt.imshow(digits.images[1796],cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

from sklearn import svm
svc= svm.SVC(gamma=0.001,C=100.0)
train=svc.fit(digits.data[0:1790],digits.target[0:1790])
print(train,'\n')
train_result=train.predict(digits.data[1791:1797])
print (train_result,'\n')


