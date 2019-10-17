# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:13:08 2019

@author: Ryan_Kelly
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('Pokemon.csv',index_col = 0 ,encoding ='cp1252')

plt.figure(figsize=(10,6))

sns.lmplot(x='Attack', y='Defense',data=df)
