'''Python: Machine Learning🤖'''

# Machine learning involves using 
# computers to predict outcomes by 
# studying data to learn patterns

'''Mean, Median & Mode'''

# Find the mean of 15 numbers
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,85,92]

print((99+86+87+88+111+86+103+87+94+78+77+85+86+85+92) / 15)

total = 0
for i in speed:
  total = total + i
  
print(total/len(speed))

# Find the mean using numpy
import numpy as np

print(np.mean(speed))

# Median
print(np.median(speed))

# Mode
from scipy import stats

print(stats.mode(speed))



'''Standard Deviation'''

# The standard deviation is a measure
# of how far from the mean most of 
# the values in a distribution are

import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,85,92]

print(np.std(speed))

# Find the variance

print(np.var(speed))

# Finding the square root of the variance
# will give the standard deviation

print(np.var(speed)**0.5)



'''Percentiles'''

# This is a number that a given 
# percent of the values in a set are
# lower than.

import numpy as np

years = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

a = np.percentile(years, 75)
print("The 75th percentile: ", a)

b = np.percentile(years, 90)
print("The 90th percentile: ", b)



'''Data Distribution'''

# Use numpy to create a large random
# data distribution

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 5, size = 500)
plt.hist(x, 5)
plt.show()

# Create and visualize a larger array
y = np.random.uniform(5, 10, size = 10000)
plt.hist(y, 100)
plt.show()


'''Normal Data Distribution'''

import numpy as np
import matplotlib.pyplot as plt

dist = np.random.normal(10, 2, 100000)

plt.hist(dist, 100)
plt.show()




'''Scatter Plot'''

import numpy as np
import matplotlib.pyplot as plt

x = [4,12,7,12,2,9,14,5,6,10,
     8,11,3,17,8]
y = [89,86,84,82,97,88,82,95,93,84,
     84,89,103,87,89]

plt.scatter(x, y)
plt.show()

# Scatter plot with 1000 points
x = np.random.normal(12, 2, 1000)
y = np.random.normal(24, 4, 1000)

plt.scatter(x, y)
plt.show()


'''Machine Learning: Linear Regression'''

# use SciPy to draw a regression line
# for the ages (x) and speed (y) of
# 15 cars

x = [4,12,7,12,2,9,14,5,6,10,
     8,11,3,17,8]
y = [89,86,84,82,97,88,82,95,93,84,
     84,89,103,87,89]

from scipy import stats

slope, intercept, r, p, std_err = stats.linregress(x, y)

m, c = slope, intercept

def regfunc(x):
  return m * x + c

model = list(map(regfunc, x))

plt.plot(x, model)
plt.scatter(x, y)

plt.show()





m, c, r, p, std_err = stats.linregress(x, y)
print(r)

# 'r' represents the relationship or correlation
# between x and y. 1 or -1 represent perfect
# correlation, 0 means no correlation.


# There is some correlation and therefore linear
# regression can be used to predict future outcomes:

def predfunc(x):
  return m * x + c

print(predfunc(10))


# An example where linear regression would not
# be the best to predict outcomes

x1 = [40,22,37,12,9,44,35,16,10,
     18,29,30,55,37,40]
y1 = [89,86,95,82,97,88,82,95,88,84,
     84,99,90,87,89]

m, c, r, p, std_err = stats.linregress(x1, y1)

def lrfunc(x):
  return m * x + c

model2 = list(map(lrfunc, x1))

# Logistic regression does not represent 
# the data well, correlation value is very low
plt.plot(x1, model2)
plt.scatter(x1, y1)
print(r)



'''Polynomial Regression'''

# Polynomial regression can be a 
# better way to fit non linear data

# Dataset for cars speeds at a 
# toolbooth and hour of the day

x = [1,2,3,5,6,7,8,10,11,12,13,14,
     15,16,17,18,19,20,21,22]

y = [100,90,80,75,60,55,60,60,75,77,
     80,82,85,88,90,95,98,99,99,100]

import numpy as np 
import matplotlib.pyplot as plt


model = np.poly1d(np.polyfit(x,y,3))
line = np.arange(1,22, 0.21)
#print(line)

plt.scatter(x, y) 
plt.plot(line, model(line))

plt.show()

'''R-squared'''
# The r-squared value will indicate 
# how strongly related x and .y are.
# 0 means no correlation, 1 is 100%
# correlation:

from sklearn.metrics import r2_score

model = np.poly1d(np.polyfit(x, y, 3))

r2 = r2_score(y, model(x))

print(r2)
# A high r-squared score indicates 
# that polynomial regression 
# represents the data well

# Make predictions: speed of a car
# at 09:00

print(model(9))

# An example where polynomial 
# regression 

x = [5,95,48,76,15,22,82,15,52,71,
     27,9,45,91,19,88,34,51,33,57]
y = [59,69,11,98,35,53,17,67,39,55,
     8,46,72,53,66,21,76,54,89,51]

import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import r2_score

model = np.poly1d(np.polyfit(x, y, 3))
line = np.linspace(5,95,100)

plt.scatter(x, y)
plt.plot(line, model(line))

plt.show()

# R-squared
print(r2_score(y, model(x)))

# A low r-squared means low
# correlation. The data is not 
# suitable for polynomial regression 




'''Multiple Regression'''

import pandas as pd
from sklearn.linear_model import LinearRegression

cars_csv = "https://www.w3schools.com/python/cars.csv"
df = pd.read_csv(cars_csv)

h = df.head()
print(h)

# Multiple regression makes it 
# possible to predict an output ('y') 
# (such as CO2 emissions of different
# cars from multiple inputs ('X') 
# (e.g, Volume, Weight...)

X = df[["Volume", "Weight"]]
y = df["CO2"]

#print(X.head(), "\n", y.head())
# Using the LinearRegression function
# To create and fit a model

lrmodel = LinearRegression()
lrmodel.fit(X, y)

# Predict CO2 emissions with weight 
# & volume

pred_CO2 = lrmodel.predict([[2500, 
                             1400]])

print(pred_CO2)

"""Coefficient"""
# The coefficient describes the
# relationship between the unknown 
# and independent variables

a = lrmodel.coef_

print(lrmodel.coef_)
print("Coefficient of 'Volume': ", 
      a[0], "\n", 
      "Coefficient of 'Weight': ", 
      a[1])
print("Model: CO2 = ", '%.7f'%(a[0]),
      "Volume + ", '%.7f'%(a[1]), 
      "Weight")




'''Machine Learning: Scale'''

# Scaling is done to make different 
# features comparable for machine
# learning

import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("https://www.w3schools.com/python/cars2.csv")
print(df.head(), df.shape)

# the standardization formula of 
# scaling uses the following formula
# newValue = (originalValue - mean)/standardDeviation

scale = StandardScaler()

X = df[["Volume", "Weight"]]
X_scaled = scale.fit_transform(X)
y = df["CO2"]

#print(X_scaled)

lrmodel = linear_model.LinearRegression()
lrmodel.fit(X_scaled, y)

# to predict unknown values of CO2,
# we need to scale Volume & Weight

scaled_x = scale.transform([[1.3, 2300]])

co2 = lrmodel.predict([scaled_x[0]])
print(co2)
print(scaled_x)




'''Machine learning: Train/Test'''

# split data into training (usually 
# 80%) and test (remaining data) 
# sets to evaluate models

import matplotlib.pyplot as plt 
from numpy import random, linspace
from numpy import poly1d, polyfit
from sklearn.metrics import r2_score

# the following data set represents
# shoppers' behavior in a store. 
# x = minutes spent before buying
# y = amount spent on purchase

random.seed(2)

x = random.normal(3, 1, 100)
_y = random.normal(150, 40, 100)
y = _y/x

#plt.scatter(x, y)
plt.show()

# split into training and test sets

x_train = x[0:80]
y_train = y[:80]

x_test = x[80:]
y_test = y[-20:]

#plt.scatter(x_train, y_train)
plt.show()
#plt.scatter(x_test, y_test)
plt.show()

# To fit the data: the plot suggests 
# that polynomial regression can
# be used to represent the data

model = poly1d(polyfit(x_train, 
                       y_train, 3))

# Plot model and data to compare fit
xpoints = linspace(0, 6, 100)

plt.scatter(x, y)
plt.plot(xpoints, model(xpoints))

plt.show()


# Check relationship between x and y
r2 = r2_score(y_train, model(x_train))
print(r2) #shows a decent relationship

# test model relationship to test set

r2_test = r2_score(y_test, 
                   model(x_test))
print(r2_test) # shows a relationship

# Make a test prediction for a 
# customer who spent 5 minutes before
# buying

print(model(5)) # corresponds to plot





'''Machine Learning: Decision Tree'''

# Decision trees are flow charts that
# can be used to make predictions by
# learning from prior experience 

import pandas as pd
import pydotplus
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg

df = pd.read_csv("https://docs.google.com/spreadsheets/d/1ukc5L5JeqktUDps4KSq7qS6JLkPEpCKysR9S44IzO04/export?format=csv&gid=0")

# Use the pandas method 'map()' to
# Convert non numerical columns. 
# Required for decision tree

country = {'UK':0, 'USA':1, 'N':2}
go = {'NO':0, 'YES':1}

df["Nationality"] = df["Nationality"].map(country)
df["Go"] = df["Go"].map(go)

print(df.head())


# Separate data into features and
# target
features = ["Age", "Experience", "Rank", 
            "Nationality"]
target = "Go"

X = df[features]
y = df[target]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

dotdata = tree.export_graphviz(dtree, 
                            out_file = None,
                            feature_names = features)
graph = pydotplus.graph_from_dot_data(dotdata)
graph.write_png("DecisionTreeModel.png")

image = pltimg.imread("DecisionTreeModel.png")
plotimage = plt.imshow(image)
plt.show

