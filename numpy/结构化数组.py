#!@Author : Sanwat
#!@File : .py
import numpy as np

structured = np.array([(1,'First',0.5,1+2j),(2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)],dtype=('i2,a6,f4,c8'))
print (structured,'\n')

structured2= np.array([(1,'First',0.5,(1+2j)),(2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)],dtype=('int16,a6,float32,complex64'))
print (structured2,'\n')
#下面开始索引
a= structured2[1]
print (a)

b= structured2['f3']
print(b,'\n')

structured3 = np.array([(1,'First',0.5,1+2j),(2,'Second',1.3,2-2j),
                       (3,'Third',0.8,1+3j)],dtype=[('id','i2'),('position','a6'),('value','f4'),('complex','c8')])
print (structured3)
'''
自定义索引
'''
structured3.dtype.names =('id','order','value','complex')
display1= structured3['id']
print (display1,'\n')
display2= structured3['order']
print(display2,'\n')
display3= structured3['value']
print (display3,'\n')
display4= structured3['complex']
print(display4)
