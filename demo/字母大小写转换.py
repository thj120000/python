#!@Author : Sanwat
#!@File : .py
str = input("请输入字符串：")
b = []
for i in str:
    if 'a' <= i <= 'z':
        b.append(i.upper())
    elif 'A'<=i<='Z':
        b.append(i.lower())
    else:
        b.append(i)
print(''.join(b))
