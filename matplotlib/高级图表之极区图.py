#!@Author : Sanwat
#!@File : .py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
N= 8
theta= np.arange(0.,2*np.pi,2*np.pi/N)
raddi= np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025,0.025,0.95,0.95],polar= True)
colors= np.array(
    ['red','white','green','yellow','navy','brown','violet','blue']
)
plt.bar(theta,raddi,width=(2*np.pi/N),bottom= 0.0,color=colors)
plt.show()