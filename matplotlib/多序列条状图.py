#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(1)
index= np.arange(5)
value1= [5,7,5,3,4]
value2= [6,6,4,5,7]
value3= [5,6,5,4,6]
bw= 0.3
plt.axis([0,5,0,8])
plt.title('A Multiseries Bar Chart',fontsize= 20)
plt.bar(index,value1,bw,color='b')
plt.bar(index+bw,value2,bw,color='r')
plt.bar(index+2*bw,value3,bw,color='g')
plt.xticks(index+bw,['A','B','C','D','E'])
plt.show()
#横向
plt.figure(2)
plt.title('A Multiseries Horizontal Bar Chart',fontsize=18)
plt.barh(index,value1,bw, color='k')
plt.barh(index+bw,value2,bw,color= 'r')
plt.barh(index+2*bw,value3,bw,color= 'g')
plt.yticks(index+bw,['a','b','c','d','e'])
plt.show()