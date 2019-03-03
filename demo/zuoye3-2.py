#!@Author : Sanwat
#!@File : .py
# -*- coding: UTF-8 -*-
import math
print ("输入圆半径r=：")
r= float(input())
print ("输入圆柱高h=：")
h= float(input())

c = 2*math.pi*r
s1 = math.pi*r*r
s2 = 4*math.pi*r*r
v1 = 4/3*math.pi*r*r*r
v2 = math.pi*r*r*h

print ("圆面积=",s1)
print ("圆周长=",c)
print ("圆球表面积=",s2)
print ("圆球体积=",v1)
print ("圆柱体积=",v2)
