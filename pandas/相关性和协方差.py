#!@Author : Sanwat
#!@File : .py
import numpy as py
import pandas as pd

seq1= pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq2= pd.Series([1,2,3,4,4,3,2,1],['2006','2207','2008','2009','2010','2011','2012','2013'])
print (seq1,'\n')
print (seq2,'\n')
corr= seq2.corr(seq1)
print ('相关性：',corr,'\n')
cov= seq2.corr(seq1)
print ('协方差：',cov,'\n')

frame= pd.DataFrame(
    [[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
    index= ['red','blue','yellow','white'],
    columns= ['ball','pen','pencil','paper']
)
print (frame,'\n')
corr1= frame.corr()
print ('相关性：','\n')
print (corr1,'\n')
cov1= frame.cov()
print ('协方差：','\n')
print (cov1,'\n')
