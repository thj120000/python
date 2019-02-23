#!@Author : Sanwat
#!@File : .py

import numpy as np
from math import sin
from numpy.polynomial import Chebyshev
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

'''
def  g(y):
    #return sin(((x - 1) * 5) ** 2) + (sin((x - 1) * 5)) ** 2
    y = (x - 1) * 5
    return sin(y ** 2) + sin(y) ** 2
n=100
x1=np.linspace(-1,1,n)
#polynomial正藏插值区间x2=Chebyshev.basis(n).roots()#Chebyshev进行插值
xd=np.linspace(-1,1,1000)
c1=Chebyshev.fit(x1,f(x1),n-1,domain=[-1,1])
c2=Chebyshev.fit(x2,f(x2),n-1,domain=[-1,1])
print(u"插值多样式的最大误差：")
print(u"等距离取样点：",abs(c1(xd)-f(xd)).max())
print(u"切比雪夫节点：",abs(c2(xd)-f(xd)).max())



def f(x):
    return 1.0 / (1 + 25 * x ** 2)


n = 11
x1 = np.linspace(-1, 1, n)
x2 = Chebyshev.basis(n).roots()
xd = np.linspace(-1, 1, 200)

c1 = Chebyshev.fit(x1, f(x1), n - 1, domain=[-1, 1])
c2 = Chebyshev.fit(x2, f(x2), n - 1, domain=[-1, 1])

print("插值多项式的最大误差：")
print("等距离取样点：", abs(c1(xd) - f(xd)).max())
print("契比雪夫节点：", abs(c2(xd) - f(xd)).max())
'''