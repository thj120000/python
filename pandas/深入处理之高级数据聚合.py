#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
frame= pd.DataFrame(
    {
        'color':['white','red','green','red','green'],
        'price1':[5.56,4.20,1.30,0.56,2.75],
        'price2':[4.75,4.12,1.60,0.75,3.15]
    }
)
print (frame,'\n')
sums= frame.groupby('color').sum().add_prefix('tot_')#计算价格总和
print (sums,'\n')
'''
merge()将两个对象的内容合并
'''
merge1= pd.merge(frame,sums,left_on='color',right_index=True)#将价格总和的列表添加到原始列表
print (merge1,'\n')
'''
transform把sum（）求得的值每一行列出
'''
sum2= frame.groupby('color').transform(np.sum).add_prefix('tot_')
print (sum2,'\n')

'''
apply()函数适用于更一般的Groupby操作，完全实现了split-apply-combine机制
'''
frame2= pd.DataFrame(
    {
        'color':['white','black','white','white','black','black'],
        'status':['up','up','down','down','down','up'],
        'value1':[12.33,14.55,22.34,17.84,23.40,18.33],
        'value2':[11.23,31.80,29.99,31.18,18.25,22.44]
    }
)
print (frame2,'\n')
group2= frame2.groupby(['color','status']).apply(lambda x:x.max())
print (group2,'\n')
reindex={
   0: 'first',
   1:'second',
   2:'third',
   3:'fourth',
   4:'fifth',
   5:'sixth'
}

group3= frame2.rename(index= reindex)
print (group3,'\n')

temp= dar