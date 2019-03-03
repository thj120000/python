#!@Author : Sanwat
#!@File : .py
import math

def isprime():
    for n in range (1,100):
        for i in range (2,n):
            if n % i ==0:
               # print (n,"不是一个素数")
                break
        else:
            print (n,"是一个素数")
#return x

isprime()