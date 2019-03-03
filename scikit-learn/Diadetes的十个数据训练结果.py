#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets

diadetes= datasets.load_diabetes()

x_train= diadetes.data[:-20]
y_train= diadetes.target[:-20]#被测过的结果值
x_test= diadetes.data[-20:]
y_test= diadetes.target[-20:]#实际的结果值

for f in range (0,10):
    x0_text=x_test[:,f]#选出要被测得第一列的所有值
    x0_train= x_train[:,f]#选出第一列被测过的所有值

    x1_text= x0_text[:,np.newaxis]#选出要被测的第一列的所有更新值
    x1_train= x0_train[:,np.newaxis]#选出被测过的第一列的所有更新值，

    linreg= linear_model.LinearRegression()
    line_train= linreg.fit(x1_train,y_train)#用已被测过的第一列的所有更新值和原本的数据结果训练
    predict_result= linreg.predict(x1_text) #确定出要被测的第一例的所有更新值的结果

    plt.subplot(5,2,f+1)
    plt.scatter(x1_text,y_test,color='k')#读取点，横坐标为更新过的预测点，纵坐标为原来的实际点
    plt.plot(x1_text,predict_result,color='b',linewidth=3)#预测结果，横坐标为更新过预测点，纵坐标为训练预测结果
plt.show()