#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime
from matplotlib.dates import DateFormatter

# Read from the CSV file
data = read_csv('GoogleCloudTest.csv')


# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

# Horizontal Boxplot
plt.figure()
plt.boxplot(y,1, vert=False)
plt.gcf().autofmt_xdate()
plt.xlabel("CPU Usage %")
plt.title('GodMode: Horizontal Box Plot of CPU Usage %')

#General 
plt.legend()
plt.show()