
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

#Partition data into "boxes"
bins = [0,10,20,30,40,50,60,70,80,100]

# Histogram showing temperature
plt.hist(y, bins, normed=1, histtype='bar', rwidth=0.9)
plt.gcf().autofmt_xdate()
plt.xlabel("Temperature in C")
plt.ylabel("Probability")
plt.legend()
plt.title('GodMode: Histogram showing Temperature')
plt.show()
