#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime


# Read from the CSV file
data = read_csv('Test.csv')

# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

# Find the slope and intercept of the best fit line
slope, intercept = np.polyfit(x, y, 1)

line = [slope * i + intercept for i in x]
# Linear Regression
plt.figure()
plt.plot(x, y, 'ro')
plt.plot(x, line, 'b')
plt.gcf().autofmt_xdate()
plt.ylabel("Temperature in C")
plt.xlabel("CPU Usage %")
plt.title('GodMode: Linear regression')

#General 
plt.legend()
plt.show()