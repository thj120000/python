#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

nframe= pd.DataFrame(np.arange(25).reshape(5,5))
print (nframe,'\n')

'''
利用permutation()函数创建一个顺序包含（0-4）的顺序随机的数组。
'''
new_order= np.random.permutation(5)
print (new_order,'\n')
'''
利用take()函数把这个随机数组传给对象，即可以打乱排序
'''
nframe1= nframe.take(new_order)
print (nframe1,'\n')
'''
或者对部分进行排序操作，例如选择2-4
'''
new_order1=[3,2,4]
nframe2= nframe.take(new_order1)
print (nframe2,'\n')

'''
随机取样：使用np.random.randint()函数
'''
sample= np.random.randint(0,len(nframe),size=3)
print (sample,'\n')
nframe3=nframe.take(sample)
print (nframe3,'\n')

