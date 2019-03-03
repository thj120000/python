#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import sqlite3

frame= pd.DataFrame(
    np.arange(20).reshape(4,5),
    columns=['white','red','blue','black','green']
)
print(frame,'\n')

#连接SQLite3数据库
engine = create_engine('sqlite://foo.db')