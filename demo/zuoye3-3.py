#!@Author : Sanwat
#!@File : .py

# -*- coding: UTF-8 -*-
import math
print ("输入三角形的三边：")
print ("a=")
a = float(input())
print ("b=")
b = float(input())
print ("c=")
c = float(input())

cosangle= (a*a+b*b-c*c)/(2*a*b)
angle = math.acos(cosangle)*180/math.pi
print ("夹角C的余弦值为：",cosangle)
print ("夹角C的度数为：",angle)
