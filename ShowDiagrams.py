#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime
from matplotlib.dates import DateFormatter

# Read from the CSV file
data = read_csv('rawdata.csv')


# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

#Plot Histogram
plt.plot_date(t,x, 'b-', color='r')
plt.plot_date(t,y, 'g-', color='b')
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
# Partition data into "boxes"
bins = [0,10,20,30,40,50,60,70,80,100]
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
# Find the slope and intercept of the best fit line
slope, intercept = np.polyfit(x, y, 1)
line = [slope * i + intercept for i in x]
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