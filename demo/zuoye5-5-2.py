#!@Author : Sanwat
#!@File : .py
from functools import  reduce

def func(n):
        a = n % 5
        b = n % 3
        if (a == 0 and b == 0):
            return True

def add(x,y):
    return x+y

def power (z):
    return z*z*z

print("100以内可以同时被3和5整除的数有：")
print (list(filter(func,range (0,100))))
print("0-100所有奇数的和为：")
print (reduce(add,range (0,100),-2450))
print("0-100所有偶数的立方：")
print (list (map(power,range (1,101))))