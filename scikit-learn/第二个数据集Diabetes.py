#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
diabetes= datasets.load_diabetes()
#print (diabetes,'\n')
'''
该数据集包含442位病人的生理数据以及一年之后的病情发展情况，后者即为目标值。
前十列值为生理数据，分别表示以下特征：
年龄，性别，体制指数，血压，S1,S2,S3,S4,S5,S6(六种血清的化验数据）
调用data，显示第一位病人的前十个数据
'''
print(diabetes.data[0],'\n')#这些值每个先做了均值处理，然后又用标准差乘以个体数量来调整了数值范围，因此它们之和为1
s=np.sum(diabetes.data[:,0]**2)#先自己平方运算，在求和
print(s,'\n')
#利用target属性 显示疾病进展的数据
print(diabetes.target,'\n')#打印出442个数据
'''
线性回归：最小平方回归
指的是用训练集数据创建线性模型的过程。例如y=a*x+c
x为训练集，y为目标值，a为斜率，c为模型所对应的直线的截距
接下来，我们利用scikit-learn库的线性回归预测模型，linear_model模块
'''
from sklearn import linear_model
linreg= linear_model.LinearRegression()#利用LinearRegression()构造函数创建预测模型
'''
把前422位病人病情的数据集作为训练集，后20位病人作为测试集
'''
x_train=diabetes.data[:-20]
y_train=diabetes.target[:-20]
x_test=diabetes.data[-20:]
y_test=diabetes.target[-20:]

line_train=linreg.fit(x_train,y_train)#调用fit()对训练集做训练
'''
调用coef_属性,可以观察其回归系数b
'''
b= line_train.coef_
print("回归系数：",b)

predict_result= linreg.predict(x_test)
print("训练结果：",predict_result,'\n')
print ("实际结果：",y_test,'\n')
fangcha=linreg.score(x_test,y_test)
print ("方差：",fangcha)
