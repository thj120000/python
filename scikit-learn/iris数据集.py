#!@Author : Sanwat
#!@File : .py

'''
有监督学习：训练集包含作为预测结果的额外的信息属性，这些信息可以作为指导模型对新数据做出跟已有数据类似的预测结果。包括分类和回归
无监督学习：训练集 数据由一系列输入值x组成，其目标值未知。包括聚类和降维

****有监督学习****
1，用Iirs 数据集讲解分类
K-近邻分类器
支持向量分类（SVC)
2,用Diabetes 数据集介绍回归算法
线性回归
支持向量回归(SVR)
'''
from sklearn import datasets
'''
iris数据集：鸢尾花数据集
这些数据时安德森通过直接测量鸢尾花花朵各部分得到的，确切的来说，这些数据表示的是萼片和花瓣的长宽。
'''
import matplotlib.pyplot as plt
iris= datasets.load_iris()
'''
输出结果包含150个元素的数组，每个元素包括四个数值：分别为萼片和花瓣的数据
'''
print(iris.data,'\n')
#访问target 可以知道每一种花卉的种类
'''
输出结果包含150个数值，0，1，2分别代表三种不同的鸢尾花花卉
'''
print(iris.target,'\n')
#利用target_names属性,访问0，1，2所代表的花卉的类别
print(iris.target_names,'\n')
'''
接下来用散点图来表示出三种花卉种类，x轴表示萼片的长度，y轴表示的花卉的类别
'''
x= iris.data[:,0]#x-Axis -  萼片长度。表示所有行的第一个数据，即第一列
y= iris.data[:,1]#y轴  --花萼宽带。表示所有行的第二个数据，即第二列
species= iris.target
x_min, x_max= x.min()-0.5,x.max()+0.5
y_min , y_max = y.min()-0.5, y.max()+0.5

#获取图像scatter(）
plt.figure(1)
plt.subplot(121)
plt.title('Iris Dataset - Classification By Sepal Sizes',fontsize=12,color='r')
plt.scatter(x,y,c=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.xlim(x_min,x_max)#x轴的显示长度范围
plt.ylim(y_min,y_max)#y轴的显示长度范围
#x,y轴显示上的内容为空
#plt.xticks(())
#plt.yticks(())

plt.subplot(122)
x2= iris.data[:,2]#取所有行的第三个数据，即第三列
y2= iris.data[:,3]#取所有行的第四个数据，即第四列
x2_min, x2_max= x2.min()-0.5,x2.max()+0.5
y2_min , y2_max = y2.min()-0.5, y2.max()+0.5

plt.title('Iris Dataset - Classification By Sepal Sizes',fontsize=12,color='r')
plt.scatter(x2,y2,c=species)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.xlim(x2_min,x2_max)
plt.ylim(y2_min,y2_max)
plt.savefig('鸢尾花数据对比图.jpg')
plt.show()
