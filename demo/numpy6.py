#!@Author : Sanwat
#!@File : .py
import numpy as np#导入画图模块
from matplotlib.pyplot import plot,show#导入matplotlib模块的画图和显示函数
money=np.zeros(10000)#先将赌博次数的每一次的money初始化为0
money[0]=1000#表示刚开始有1000元现金
result=np.random.binomial(5,0.5,size=len(money))#二项分布的10000次成功的次数
#遍历10000数，更新每一次的moeny值存储
for i in range(1,len(money)):#从1到10000进行遍历
    if result[i]<3:
        money[i]=money[i-1]-8
    else:
        money[i]=money[i-1]+8
print(result.min(),result.max())#打印5次抛硬币最多出现正面，和最少出现正面的次数
print(money.max(),money.min())#打印可能出现钱最多，最少的情况
plot(np.arange(len(money)),money)#画图
show()#显示输出结果：
