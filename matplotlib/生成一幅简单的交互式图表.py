#!@Author : Sanwat
#!@File : .py
import numpy as np
import matplotlib.pyplot as plt
'''
显示图线
'''
#print (plt.plot([1,2,3,4]))
#plt.show()
'''
显示坐标点
'''
plt.plot([1,2,3,4],[1,4,9,16],'ro')

'''
用title 函数增加标题
'''
plt.title('My first plot')
plt.axis([0,5,0,20])
plt.show()