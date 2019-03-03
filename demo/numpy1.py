#!@Author : Sanwat
#!@File : .py
import numpy as np
arrll= 5-np.arange(1,13).reshape(4,3)
print (arrll)
print ("所有元素的和:",arrll.sum())
print ("每一列元素的和:",arrll.sum(axis=0))
print ("对每个元素求累积和:",arrll.cumsum())
print("每一列求累积和:",arrll.cumsum(axis=0))
print("每一行的累计积:",arrll.cumprod(axis=1))
print("所有元素的最小值:",arrll.min())
print("每一列的最大值:",arrll.max(axis=0))
print("所有元素的平均值:",arrll.mean())
print("每一行元素的均值:",arrll.mean(axis=1))
print("每一列的中位数:",np.median(arrll,axis=0))
print("所有元素的方差:",arrll.var())
print("每一行的标准差：",arrll.std(axis=1))
