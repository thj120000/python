#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
1,直方图
'''
#random.randint ()函数生成100个0-100 的随机数作为样本
pop= np.random.randint(0,100,100)
print (pop,'\n')
'''
(n,bins,patches)
'''
n,bins,patches= plt.hist(pop, bins=20)#默认分为10面元，设置bins= 20，则会分为20个面元
plt.show()