# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:11:52 2015

@author: Joseph
"""
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import Toydata


NumberSamples=2000;

a=np.matrix([-1,1,2,1,1,-3,1])

a=a.T
Out=Toydata.MakeToyData(a,NumberSamples)

#training data
Xtrain=Out[0]
ytrain=Out[1]



#plot 
fig = plt.figure()
fig.suptitle('Not Linearly Separable Toy Data', fontsize=14, fontweight='bold')
plt.plot(Xtrain[ytrain==1,0],Xtrain[ytrain==1,1],'bo', Xtrain[ytrain==2,0], Xtrain[ytrain==2,1],'ro') 