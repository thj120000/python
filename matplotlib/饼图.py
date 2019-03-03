#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(1)
labels= ['Nokia','Sansung','Apple','Lumia']#设置名字
values= [10,30,45,15]
colors= ['yellow','green','red','blue']#颜色
'''
explode 关键字，设置脱离饼的情况（0-1）
'''
explode=[0.3,0,0,0]#将第一个变量脱离
'''
starttangle关键字调整饼图的选择角度
shadow 关键字添加阴影
autopct 关键字添加图块所占百分比
'''
plt.pie(values,labels=labels,colors=colors,explode=explode,startangle=180,shadow=True,autopct='%1.1F%%')
plt.axis('equal')
plt.title('my first pie',fontsize=20,color='r')
plt.show()

'''
plt.figure(2)
plt.pie(values,labels=labels,colors=colors,)
'''