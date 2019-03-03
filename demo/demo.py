
# !/usr/bin/python
# -*- coding: UTF-8 -*-
my_list = [1, 3, 2, 5, 61, 123]

# 从小到大排序
my_list.sort()
print(my_list)

# 从大到小排序
my_list.sort(reverse=True)
print(my_list)

'''
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="yourusername",  # 数据库用户名
    passwd="yourpassword"  # 数据库密码
)

print(mydb)



name = '0123456789'
print(name[:-5:-3])


n=0
s= str( input())
for i in range (0,len(s)):
    m= s[i:i+3]
    if (m=="bob"):
        n=n+1
    i = i + 1

print(n)

m=0

for n in range (0,len(s)):
    if (n=="b" and n+1=="o" and n+2=="b"):
        m=m+1
    n=n+1
print (m)


print ("从键盘输入华氏温度：")
F = float (input())
temp = F
print ("当前的华氏温度：",temp)
c= 5/9*(temp - 32)
print ("当前的摄氏温度：",c)



print
"a + b 输出结果：", a + b
print
"a * 2 输出结果：", a * 2
print
"a[1] 输出结果：", a[1]
print
"a[1:4] 输出结果：", a[1:4]

if ("H" in a):
    print
    "H 在变量 a 中"
else:
    print
    "H 不在变量 a 中"

if ("M" not in a):
    print
    "M 不在变量 a 中"
else:
    print
    "M 在变量 a 中"

print
r'\n'
print
R'\n'
'''