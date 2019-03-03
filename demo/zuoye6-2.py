#!@Author : Sanwat
#!@File : .py
import re
s = input("请输入小写字符串：")
test = r'a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*'
ans = re.findall(test, s)
ans = sorted(ans, key=len, reverse=True)
print("Longest substring in alphabetical order is:", ans[0])
