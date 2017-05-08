#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime
from matplotlib.dates import DateFormatter
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model

# Read from the CSV file
data = read_csv('rawdata.csv')


# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

#Plot Histogram
plt.plot_date(t,x, 'b-', color='b')
plt.plot_date(t,y, 'g-', color='r')
plt.legend()
plt.gcf().autofmt_xdate()
plt.xlabel("Time")
plt.title('GodMode: Time Series')

# Vertical Boxplot
plt.figure()
plt.boxplot(y,1)
plt.gcf().autofmt_xdate()
plt.ylabel("Temperature in C")
plt.title('GodMode: Vertical Box Plot of Temperature')

# Horizontal Boxplot
plt.figure()
plt.boxplot(y,1, vert=False)
plt.gcf().autofmt_xdate()
plt.xlabel("CPU Usage %")
plt.title('GodMode: Horizontal Box Plot of CPU Usage %')

# Histogram - CPU Usage
bins = [0,10,20,30,40,50,60,70,80,100] # Partition data into "boxes"
plt.figure()
plt.hist(x, bins, normed=1, histtype='bar', rwidth=0.9)
plt.gcf().autofmt_xdate()
plt.xlabel("CPU Usage %")
plt.ylabel("Probability")
plt.title('GodMode: Histogram Showing CPU USAGE')

# Histogram - Temperature in C
plt.figure()
plt.hist(y, bins, normed=1, histtype='bar', rwidth=0.9)
plt.gcf().autofmt_xdate()
plt.xlabel("Temperature in C")
plt.ylabel("Probability")
plt.title('GodMode: Histogram showing Temperature')

# Linear regression
slope, intercept = np.polyfit(x, y, 1)
line = [slope * i + intercept for i in x]
plt.figure()
plt.plot(x, y, 'ro')
plt.plot(x, line, 'b')
plt.gcf().autofmt_xdate()
plt.ylabel("Temperature in C")
plt.xlabel("CPU Usage %")
plt.title('GodMode: Linear regression')


# Cross Validation
lr = linear_model.LinearRegression()
predicted = cross_val_predict(lr, np.transpose(np.matrix(x)), np.transpose(np.matrix(y)), cv=10)
plt.figure()
plt.scatter(y, predicted)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b-',color='r', lw=2)
plt.xlabel('Measured')
plt.ylabel('Predicted')

#General 
plt.legend()
plt.show()