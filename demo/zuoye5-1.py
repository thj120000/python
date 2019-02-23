#!@Author : Sanwat
#!@File : .py
import math

def evalQuadratic(a,b,c,x):
    s=a*x*x+b*x+c
    print ("返回值为：",s)
    return s
print ("请输入a,b,c和x的值：")
print ("a=")
q= float (input())
print ("b=")
w= float (input())
print ("c=")
e= float (input())
print ("x=")
r= float (input())
evalQuadratic(q,w,e,r)