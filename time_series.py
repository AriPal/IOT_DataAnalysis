
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

# Labels 


#Plot data into diagram
plt.plot_date(t,x, 'b-')
plt.plot_date(t,y, 'g-')
plt.gcf().autofmt_xdate()
plt.show()


