#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
dframe= pd.DataFrame(
    {
        'color':['white','white','red','red','white'],
        'value':[2,1,3,3,2]
    }
)
print(dframe,'\n')
'''
duplicated()函数用来检测重复的行，返回元素为布尔型，若有重复项，返回值为True,否则为False
'''
jiance= dframe.duplicated()
print (jiance,'\n')

'''
返回元素为布尔值的Series对象用处很大，特别适合过滤操作。比如寻找重复的行
'''
chongfuhang= dframe[dframe.duplicated()]
print (chongfuhang,'\n')
'''
drop_duplicated()用于返回删除重复行之后的对象
'''
dframe1=dframe.drop_duplicates()
print (dframe1,'\n')

'''
2,映射之替换元素
replace（）：替换元素
'''

print (dframe,'\n')
newcolors= {
    'rosso':'red',
    'verde':'green'
}
frame2=dframe.replace(newcolors)
print (frame2,'\n')
ser= pd.Series([1,3,np.nan,4,6,np.nan,3])
print (ser,'\n')
ser1= ser.replace(np.nan,0)
print (ser1,'\n')
'''
3,映射之添加元素
map()新建一行
'''
frame3= pd.DataFrame(
    {
        'item':['ball','mug','pen','pencil','ashtray'],
        'color':['white','red','green','black','yellow']
    }
)
print (frame3,'\n')
price= {
    'ball':5.56,
    'mug':4.20,
    'bottle':1.30,
    'scissors':0.56,
    'pen':1.30,
    'pencil':0.56,
    'ashtray':2.58
}
frame3['price']= frame3['item'].map(price)
print (frame3,'\n')
'''
4,重命名轴索引
rename（）函数
'''
reindex= {
    0:'first',
    1:'second',
    2:'third',
    3:'fourth',
    4:'fifth'
}
frame4= frame3.rename(reindex)
print (frame4,'\n')
print ('.......','\n')
#重命名各列

recolumns={
    'item':'object',
    'price':'value'
}
frame5=frame3.rename(index= reindex,columns=recolumns)
print (frame5,'\n')
'''
5，对单个变量进行替换
'''
print(frame3,'\n')
frame6= frame3.rename(index={1:'first'},columns={'item':'object'})
print (frame6,'\n')
