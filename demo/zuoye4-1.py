#!@Author : Sanwat
#!@File : .py

print ("请从键盘输入一个数：")
END  = float (input())
S=0
while (END >0):
    S= S+END
    END= END-1
print("这个数的和是",S)