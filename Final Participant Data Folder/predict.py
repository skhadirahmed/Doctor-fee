# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:34:05 2019

@author: skhad
"""

import pandas as pd

df = pd.read_excel("Final_Train.xlsx")
q = []
for x in df['Qualification']:
    q.append(x)
exp = []
for x in df['Experience']:
    x = x.split(" ")
    exp.append(int(x[0]))

f = []
for x in df['Fees']:
    f.append(x)

import numpy as np
X = np.array([q])
Y = np.array([f])
Y.reshape((1,5961))
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
y_pred = gnb.fit([exp],Y)
#y_pred.predict("BHMS, MD - Homeopathy")
import matplotlib.pyplot as plt
plt.scatter(exp,f)