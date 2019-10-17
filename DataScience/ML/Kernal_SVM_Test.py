# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:19:42 2019
Kernal SVM: Non-Linear data
@author: Ryan_Kelly
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Assign column names to the dataset
colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
irisdata = pd.read_csv(url, names=colnames)


X = irisdata.drop('Class', axis=1)
y = irisdata['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Polynomial Kernel
svclassifier = SVC(kernel='poly', degree=8)
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print("Polynomial Kernel\n")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("--------------------------------------\n")
#------------------------------------------------

# Gaussian Kernel
svclassifier = SVC(kernel ='rbf')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)

print("Gaussian Kernel\n")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("--------------------------------------\n")
#------------------------------------------------

#Sigmoid Kernel
svclassifier = SVC(kernel='sigmoid')
svclassifier.fit(X_train, y_train)

y_pred = svclassifier.predict(X_test)
print("Sigmoid Kernel\n")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("--------------------------------------\n")
