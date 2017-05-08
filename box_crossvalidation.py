#Include library
from pandas import *
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt


# Read from the CSV file
data = read_csv('rawdata.csv')

# Get Data from CSV file
t = data['Date / Time']
x = data['CPU Usage %']
data = data['Temperature C']

# lr = linear_model.LinearRegression()
# boston = datasets.load_boston()
# y = boston.target

y = data.quality(float)
print(y)


# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
# predicted = cross_val_predict(lr, boston.data, y, cv=10)

# fig, ax = plt.subplots()
# ax.scatter(y, predicted)
# ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k-', lw=2)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()




# from sklearn import datasets, linear_model
# from sklearn.model_selection import cross_val_predict
# diabetes = datasets.load_diabetes()
# X = diabetes.data[:150]
# y = diabetes.target[:150]
# lasso = linear_model.Lasso()
# y_pred = cross_val_predict(lasso, X, y)

