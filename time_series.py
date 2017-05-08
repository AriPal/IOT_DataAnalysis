
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
plt.legend()
plt.title('GodMode: Time Series')
plt.show()

