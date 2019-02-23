#!@Author : Sanwat
#!@File : .py

'''
for n in range (2,1000):
n = int (input("input number:"))
'''

for n in range (2,1000):
    fac = []
    s = 0
    for i in range (1,n):
        if n % i ==0:
            s=i+s
            fac.append(i)
    if (s==n):
        print (n,"是完数，因子为:",fac)
