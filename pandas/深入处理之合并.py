#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd

frame1= pd.DataFrame(
    {
        'id':['ball','pencil','pen','mug','ashtray'],
        'price':[12.33,11.44,33.21,21.13,33.62]
    }
)
print (frame1,'\n')

frame2= pd.DataFrame(
    {
        'id':['pencil','pencil','ball','pen'],
        'color':['white','red','red','black']
    }
)
print (frame2,'\n')
'''
应用合并函数merge()
'''
frame3= pd.merge(frame1,frame2)
print (frame3,'\n')

'''
实际中，我们需要利用on 来指定哪一列进行合并
'''
frame4= pd.DataFrame(
    {
        'id':['ball','pencil','pen','mug','ashtray'],
        'color':['white','red','red','black','green'],
        'brand':['OMG','ABC','ABC','POD','POD']
    }
)
print (frame4,'\n')
frame5= pd.DataFrame(
    {
        'id':['pencil','pencil','ball','pen'],
        'brand':['OMG','POD','ABC','POD']
    }
)
print(frame5,'\n')
frame6= pd.merge(frame4,frame5)
print (frame6,'\n')
'''
可见，上述两个不能合并，因此，我们用on选项指定合并操作所依据的基准列。
合并准则：on作为基准列，将两个共有部分表示出来，然后再合并各自部分的列。
'''
frame7= pd.merge(frame4,frame5,on='id')
print (frame7,'\n')
frame8= pd.merge(frame4,frame5,on='brand')
print (frame8,'\n')
'''
如果两个dataframe 的基准列都不一样，可以用left_on, right_on 指定两个进行合并
'''

frame5.columns=['sid','brand']
print (frame5,'\n')
frame9= pd.merge(frame4,frame5,left_on='id',right_on='sid')
print (frame9,'\n')

'''
上述合并准则默认是内链接，所以连接根据是基准列中共有部分进行合并，外连接是根据基准列将两个部分都进行合并，利用how(),
outer相当于左连接和右连接之和。
'''
frame5.columns= ['id','brand']
frame10= pd.merge(frame4,frame5,on='id',how='outer')
print(frame10,'\n')
frame11= pd.merge(frame4,frame5,on='id',how='left')
print (frame11,'\n')
frame12= pd.merge(frame4,frame5,on='id',how='right')
print (frame12,'\n')
'''
如果想合并多个健，则把多个键赋值给on选项
即就是把两个对象中都有的列合并相加。没有的部分赋值NAN
'''
frame12= pd.merge(frame4,frame5,on=['id','brand'],how='outer')
print (frame12,'\n')

'''
根据索引合并，之前的合并都是基于列合并，接下的索引合并相当于是基于行合并
'''

frame13= pd.merge(frame4,frame5,right_index=True,left_index=True)
print (frame12,'\n')
#利用join()对于索引合并
frame5.columns= ['id2','brand2']
frame14= frame4.join(frame5)
print (frame14,'\n')


