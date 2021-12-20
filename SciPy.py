'''********************************
            SciPy Tutorial🧪
***********************************'''

# SciPy (scientific python) is an
# open source python library for
# scientific computation. It has
# many functions commonly used in
# data science. It used numpy
# underneath

#import a module from scipy

from scipy import constants

print(constants.litre) # 1L to m^3

# Check scipy version:-
import scipy

print(scipy.__version__)



'''SciPy constants'''

# scipy has a sub-module of constants

from scipy import constants

print(constants.pi)

# list all the units in constants

print(dir(constants))

# Metric prefixes (SI) (to meters)

print(constants.yotta) # 1e+24
print(constants.giga) # 1e+9
print(constants.centi) # 0.01
print(constants.nano) # 1e-9

# Binary (to bytes)

print(constants.yobi) # 2^80
print(constants.gibi) # 2^30
print(constants.kibi) # 1024

# Mass (specified unit to kg) 

print(constants.gram) # 0.001
print(constants.metric_ton) # 1000
print(constants.atomic_mass)

# Angles (specified angle to radians)
print(constants.degree)
print(constants.arcmin)
print(constants.arcsec)

# Time (convert to unit to second)
print(constants.minute)
print(constants.hour)
print(constants.year)

#Length (distance - in meters)
print(constants.inch)
print(constants.mile)
print(constants.light_year)

# Pressure (to pascal) 
print(constants.atm)
print(constants.bar)
print(constants.mmHg)

# Area (unit to square meters)
print(constants.hectare)
print(constants.acre)

# Volume (unit to meter cube)
print(constants.litre, "or", 
      constants.liter)
print(constants.gallon)
print(constants.barrel)

# Speed (to m/s)

print(constants.kmh)
print(constants.mph)
print(constants.speed_of_sound)

# Temperature (unit to Kelvin)
print(constants.zero_Celsius)
print(constants.degree_Fahrenheit)

# Energy (to joules)
print(constants.electron_volt)
print(constants.calorie)
print(constants.ton_TNT)

# Power (in watts)
print(constants.horsepower, "or", constants.hp)

# Force (in Newton)
print(constants.dyne)
print(constants.pound_force)
print(constants.kilogram_force)



'''SciPy optimizers'''

# scipy optimizers are a set of 
# procedures which find the root of
# an equation or the minimum value 
# of a function. Numpy cannot 
# find the root of nonlinear equtions
# like the one below

from scipy.optimize import root
from math import cos, sin

def equation(x):
  return x + cos(x)

eqnroot = root(equation, 0)
print(eqnroot.x)

# Root had 2 required parameters: 
# equation and an initial guess

# To show all the information about
#  the solution:-

print(eqnroot)

"""\"Minimizing a Function\""""

# A function (a curve) has high and 
# low points. The highest high and
# lowest low point are global maxima 
# and global minima respectively, 
# other high and low points are local
# maxima and minima

# Finding the minimum: 

from scipy.optimize import minimize

def eqn(y):
  return y**3 + 2*y**2 + 7*y + 2

minima = minimize(eqn, 0, method="BFGS")
print(minima, "\n\n", minima.x)



'''Scipy Sparse Data'''

# sparse data is data that contains a
# lot of zeros. 
# scipy's sparse module provides 
# functions for dealing with sparse 
# data. 

# using csr, one of 2 primary sparse 
# data matrices, csc and csr

from scipy import sparse
import numpy as np
print(dir(sparse))

array = np.array([0, 0, 0, 2, 0, 1, 1,
                  0, 0, 0])

x = sparse.csr_matrix(array)
print(x)

# Counting non-zero items
arr = np.array([[0, 1, 0], [2, 0, 0], 
               [0, 0, 1]])
y = sparse.csr_matrix(arr)

count = y.count_nonzero()
print("\n\n", y)
print(count)

# Removing zeros
y.eliminate_zeros()
print(y)

# Getting rid of duplicates
y.sum_duplicates
print(y)

# Convert from csr to csc
z = y.tocsc()
print("\n\n", z)



'''SciPy Graphs'''

# Scipy provides a way of dealing 

# with graph data structures:-

# scipy.sparse has 'csgraph'

import numpy as np
from scipy.sparse import csr_matrix, csgraph

# 'connected_components' is a function

# which shows the connection between
# graph elements as a matrix

array = np.array([[0, 1, 2], 
                  [1, 0, 0], 
                  [2, 0, 0]])

matrix = csr_matrix(array)

conn_comp = csgraph.connected_components(matrix)
print(conn_comp)

# 'dijkstra' finds the shortest path 
# between the elements of a graph

print(csgraph.dijkstra(matrix, return_predecessors = False, indices = [0, 1, 2], limit = 3))


# 'floyd_warshall finds first path
# between all element pairs

print(csgraph.floyd_warshall(matrix))

# 'bellman_ford' also finds shortest
# path between all element pairs but
# can handle negative weights

array2 = np.array([[0, -1, 2], 
                   [1, 0, 0], 
                   [2, 0, 0]])

matrix2 = csr_matrix(array2)

print(csgraph.bellman_ford(matrix2))

# 'depth_first_order' returns a depth
# first travesal from a node

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

csarr = csr_matrix(arr)

print(csgraph.depth_first_order(csarr, 0))

# 'breath_first_order' gives a breath
# first traversal from a node

print(csgraph.breadth_first_order(csarr, 0))



'''Scipy Spaial Data'''
# Spatial data is data represented in a geometric space
# the 'scipy.spatial' module provides functions to work with spatial data

# Triangulation: divide a polygon into multiple triangles to compute it's area

import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt

coordinates = np.array([
  [4, 2],
  [4, 3],
  [0, 3],
  [2, 2],
  [1, 4]
])

simplices = spatial.Delaunay(coordinates).simplices

plt.triplot(coordinates[:, 0], coordinates[:, 1], simplices)
plt.scatter(coordinates[:, 0], coordinates[:, 1], c = '#e44f5c')

#Convex Hull: the smallest polygon that will cover all given points

coordinates = np.array([
    [4, 2],
    [4, 3],
    [0, 3],
    [2, 2],
    [1, 4],
    [2, 1],
    [0, 5],
    [1, 3],
    [2, 1],
    [2, 0]
])

enclosure = spatial.ConvexHull(coordinates)
hull_points = enclosure.simplices

plt.scatter(coordinates[:, 0], coordinates[:, 1])
for simplex in hull_points:
	plt.plot(coordinates[simplex, 0], coordinates[simplex, 1], '#e44f5c')

plt.show()

#KDTrees: datastructures for nearest neighbor queries, ie, find out which points are closest to a specified point:-

#KDTree() creates a KDTree object
neighborhood = [(1, -1), (2, 3), (2, -3), (-2, 3)]

kdtree = spatial.KDTree(neighborhood)

# 'query()' gives the distance to the nearest neighbour and the index location of the neighbour
location = spatial.KDTree(neighborhood).query((2, 2))

print("KDTree object: ", neighborhood, "\n", "Distance between (2, 2) and it's nearest neighbor, and neighbor's index: ", location)

#Distance Matrices: used to find various types of distance between points.

# Euclidean Distance

pointA = (1, 1)
pointB = (4, 5)

eudist = spatial.distance.euclidean(pointA, pointB)

print(eudist)

# Cityblock Distance (Manhattan Distance): distance horizontally or vertically, not diagonally

ctbdist = spatial.distance.cityblock(pointA, pointB)

print(ctbdist)

#Cosine Distance: cosine angle between two points

cosdist = spatial.distance.cosine(pointA, pointB)

print(cosdist)

#Hamming Distance

pointX = (True, False, True, True)
pointY = (False, False, True, True)

hamdist = spatial.distance.hamming(pointX, pointY)

print(hamdist)



'''SciPy Matlab Arrays'''

import numpy as np
from scipy import io

arr = np.array(np.arange(10))

# Export Matlab format:-
# (required) filename, dict 
# containing data & (optional) 
# specify whether to compress data

io.savemat('arr.mat', {"vector": arr}, 
           do_compression = False)

# Import Matlab format

matdata = io.loadmat('arr.mat')
print(matdata)

# To print only the array:-

print(matdata["vector"])



'''SciPy Interpolation'''

# this involves generating points
# between known points.

# The scipy module 'interpolate' has
# functions used in interpolation

import numpy as np 
from scipy import interpolate

# 1-D interpolation: interpolate a 
# distribution with one variable

x = np.arange(1, 10, 1)
y = 2*x + 1

interp_func = interpolate.interp1d(x,
                                   y) 

print(interp_func(np.arange
                  (2.1, 3, 0.1)))
# interpolates the values of y for 
# values of x from 2.1, 2.2... to 2.9


# Univariate Spline Interpolation:-
# involves interpolating for a
# function that has different
# definitions at different ranges

x = np.arange(10)
y = x**2 + np.sin(x) + 1

univ_func = interpolate.UnivariateSpline(x, y)

print(univ_func(np.arange(2.1, 3.1, 0.1)))


# Radial basis function interpolates
# corresponding to a fixed reference 
# point

x = np.arange(1, 10)
y = x**2 + np.sin(x) + 1

rbf_func = interpolate.Rbf(x, y)

rbf_interp = rbf_func(np.arange(3.1, 4, 0.1))

print(rbf_interp)



'''SciPy Statistical Significance Tests'''

# statistical significance shows that
# results obtained are not random

# one tailed and two tailed tests
# test for one and two alternative
# assumptions respectively

# T-test determines if there is 
# significant difference between
# the means of two variables, to
# check if they belong to the same
# distribution 

import numpy as np 
from scipy import stats

a = np.random.normal(size = 500)
b = np.random.normal(size = 500)

ttest = stats.ttest_ind(a, b)
print(ttest)

# show only the pvalue
print(stats.ttest_ind(b, a).pvalue)


# KS-test is used to know if values
# follow a distribution

kstest = stats.kstest(a, b) 

print(kstest)


# Statistical description of data:-
# use the 'describe()' function

dt = np.random.normal(size = 1000)

description = stats.describe(dt)
print(description) 
# nobs = number of observations

# Skewness and Kurtosis are the basis 
# of normality tests. 
# Skewness is a measure of data 
# symmetry. It is 0 for normal data 
# distribution
# Kurtosis is a measure of whether
# data is heavily (+ve) or 
# lightly (-ve) tailed to a normal
# distribution

skew = stats.skew(dt)
kurtosis = stats.kurtosis(dt)

print(skew, kurtosis)

# Check if data comes from a normal
# distribution

norm = stats.normaltest(dt)
print(norm)


