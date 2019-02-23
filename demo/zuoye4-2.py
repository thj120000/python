#!@Author : Sanwat
#!@File : .py
import math

print ("请从键盘输入一个整数：")
temp  = int (input())
a=temp % 2
b=temp % 3
if (a==0 and b==0):
    print("该整数可以被2和3整除")
elif (a==0 and b!=0):
    print("该整数能被2整除,不能被3整除")
elif (a!=0 and b==0):
    print("该整数能被3整除,不能被2整除")
else :
    print ("该整数不能被2和3整除")
