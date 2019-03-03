#!@Author : Sanwat
#!@File : .py

def OnlyCharNum(s):
    num =''.join([x for x in s if x.isalnum()])
    print(num)

s = 'niha  bc123 --qwer456tyui789'
OnlyCharNum(s)
print("请输入一段字符：")
y= input()
OnlyCharNum(y)