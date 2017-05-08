#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model


# Read from the CSV file
data = read_csv('Test.csv')

# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, x, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Temperature in C')
ax.set_ylabel('Predicted')
plt.show()