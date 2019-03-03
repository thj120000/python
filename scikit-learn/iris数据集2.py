#!@Author : Sanwat
#!@File : .py

'''
主成分分解
因为这个例子中有花瓣和萼片的四个数据，然而即使是3d散点图也无法整合到四个维度。
因此需要将四维降到三维，利用scikit-learn 中的fit_transform （）函数来降维，属于PCA对象
1，导入PCA模块的sklearn.decomposition
2，使用PCV构造函数，用n_components选项降维（主成分）
3，最后，调用fit_transform ()函数，传入四维的Iris 数据集作为参数
'''
import matplotlib.pyplot as plt
import matplotlib.patches as  mpatches
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris= datasets.load_iris()
#x= iris.data[:,1]
#y= iris.data[:,2]
species= iris.target
x_reduced= PCA(n_components=3).fit_transform(iris.data)#降维，降到其主要成分

#获取
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(x_reduced[:,0],x_reduced[:,1],x_reduced[:,2],c=species)
ax.set_title('Iris Dataset By PCA',size='20',color='r')
ax.set_xlabel('First Eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
#设置三个坐标的显示值为空
#ax.w_xaxis.set_xticklabels(())
#ax.w_yaxis.set_yticklabels(())
#ax.w_zaxis.set_zticklabels(())
ax.view_init(elev=30,azim=125)
plt.savefig('3D散点图.png')
plt.show()