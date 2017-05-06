
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

xnew = np.linspace(0, 10, num=41, endpoint=True)

# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
y = data['Temperature C']

# Labels 
# plt.xlabel(temper)

# Plot colorbar
# plt.colorbar() 


#Plot data into diagram
plt.plot_date(t,x, 'b-')
plt.plot_date(t,y, 'g-')
plt.gcf().autofmt_xdate()

#Title 
plt.title('GodMode: Time Series')
plt.show()


