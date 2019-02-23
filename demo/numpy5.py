#!@Author : Sanwat
#!@File : .py

import numpy as np
from numpy.polynomial import Chebyshev
import math

def g(x):
    return sin(((x-1)*5)**2)+sin((x-1)*5)**2
n=100
x1=np.linspace(-1,1,n)#polynomial正藏插值区间x2=Chebyshev.basis(n).roots()#Chebyshev进行插值
xd=np.linspace(-1,1,1000)
c1=Chebyshev.fit(x1,g(x1),n-1,domain=[-1,1])
c2=Chebyshev.fit(x2,g(x2),n-1,domain=[-1,1])
print(u"插值多样式的最大误差：")
print(u"等距离取样点：",abs(c1(xd)-g(xd)).max())
print(u"切比雪夫节点：",abs(c2(xd)-g(xd)).max())
