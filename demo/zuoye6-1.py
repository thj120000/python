#!@Author : Sanwat
#!@File : .py
import math

a = 0
for i in range (1,101):
    b=i%7
    if (b==0):
        continue
    else :
        print("{:3d}".format(i), end=' ')
        a=a+1
        if((a%10)==0):
            print("\n")


