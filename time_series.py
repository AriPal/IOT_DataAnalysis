
#Include library
import numpy as np 
from scipy import stats 
import matplotlib.pyplot as plt 
import pdb
from pandas import *
import datetime

headers = ['col1', 'col2', 'col3'] 
dtypes = [datetime, float, float] 

# Read from the CSV file
data = read_csv('GoogleCloudTest.csv', header=None, names=headers, parse_dates=True)

#parse_dates = data['Date / Time']

t = data['Date / Time']
#x = data['CPU Usage %']
#y = data['Temperature C']


#t = datetime.datetime(2012, 2, 23, 0, 0)
#t.strftime('%m/%d/%Y')

print(t)
#plt.plot(t)
#plt.show()


