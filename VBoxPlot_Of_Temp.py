
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

# Histogram of cpu_usage
plt.figure()
plt.boxplot(y,1)

plt.gcf().autofmt_xdate()
plt.ylabel("Temperature in C")
plt.legend()
plt.title('GodMode: Vertical Box Plot of Temperature')
plt.show()

