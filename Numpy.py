"""Numpy"""


import numpy

npArray = numpy.array([2,7,3,9,34,13,13, 5])
print(npArray)

#Numpy is usually imported under the alias np
import numpy as np
np_arr = np.array(["CBS", "cheese", "laugh"])
print (np_arr)

#Check Numpy version
print(np.__version__)


#Numpy Creating arrays
'''Numpy array object is called ndarray (meaning n-dimension arrays). It accepts array-like objects (lists, tuples) & converts them to ndarray'''
array1 = np.array(["1", 23, 27, "fifty-eight", 7])

print(array1)
print(type(array1))#numpy.ndarray

###########
import numpy as np 
#Numpy array dimensions '
'''An array's dimension refers to it's depth (number of nested arrays [or arrays within the array])''' 

# 0-D arrays are the elements in an array 
array0 = np.array(17) 

#1-D arrays are made up of 0-D arrays. They are the simplest & most common 

array_1 = np.array({'five': 5, 'eighteen': 18, 'twelve': 12, 'three': 3}) 
print(array_1) 
print(type(array_1))#numpy.ndarray


#2-D arrays have 1-D arrays as their elements
'''They are usually used to represent matrices or 2nd order tensors'''
array2 = np.array([(1, 3, 5, 7), (9, 7, 19, 0), (7, 18, 2, 6)])
print(array2)
print(type(array2))

#3-D arrays are made up of 2-D arrays (or matrices)
array3 = np.array([[(16, 12, 8), (81, 27, 9)], [(3, 5, 7), (4, 8, 16)]])
print(array3)
print (type(array3))

#Check number of dimensions
'''Use the 'ndim' operator to check the number of dimensions an array has'''
print(array2.ndim) #2
print(array3.ndim) #3

#n-Dim(ensional) arrays
'''An array can have any number of dimensions
The number of dimensions can be defined using the "ndmin" argument'''

array5 = np.array([7, 11, 24, 7], ndmin = 5)
print(array5)
print(array5.ndim)


#Numpy array indexing
"""Array indexing, as with Python, starts from 0"""
import numpy as np

arr = np.array([2, 4, 16, 256])

#the 1st element
print(arr[0])

#the 2nd element
print(arr[1])

#divide the 4th by the 3rd
print(arr[3]/arr[2])


#Accessing 2-D arrays
"""Use ',' to separate the index of the 1-D array and the element:"""

arr2 = np.array([[7, 14, 21], [6, 12, 24]])
print("The 3rd element of the 2nd list is {}.".format(arr2[1, 2]))

#Accessing 3-D arrays
"""Use comma (',') to separate the index of the selected 2-D array, the list, and the chosen element."""

arr3 = np.array([[[1, 3, 5], [7, 9, 11]], [[6, 4, 2], [12, 10, 8]]])

print("The 3rd element of the 1st list of the 2nd 2-D array is {}.".format(arr3[1, 0, 2]))

#Using negative indexing
print("The 3rd element of the 1st list of the 2nd 2-D array is {} by nagative indexing".format(arr3[-1, -2, -1]))


'''Numpy array slicing'''
#works like Python built in indexing: [start:end:step], which have default values 0, {length of list} and 1 respectively

import numpy as np
arr = np.array([1, 7, 37, 9, 13, 4])
print("The 1st to 4th elements are " , arr[0:5])

print("Elements of index 3 to the end: ", arr[3:])

print("Elements from the beginning of the array to index 3: ", arr[:3])

#Using negative indexing
print("The 3rd element to the 6th (not included) using negative indexing: ", arr[-4:-1])

#Step
"""Used to specify how many elements to skip in the slicing"""
arr2 =np.array([10, 9, 8, 7, 6, 5, 4, 3])

print("Every other element from index 2: ", arr2[2::2], "...\nNo end index specified so it continues to the end by default")
print("Every other element from the beginning of the array:", arr2[-8:-1:2])

"""Slicing 2-D arrays"""
arr3 = np.array([[3, 4, 5, 6, 7], [10, 12, 14, 16, 18]])

print("Element 2 to 4 from the second 1-D array: ", arr3[1, 1:4])
print("The 4th element from both 1-D array: ", arr3[0:2, 3])
print("Elements from 2 to 4 for both 1-D arrays: ", arr3[0:2, -4:-1],"\n...returns a 2-D array")




'''Numpy data types'''

#numpy has some additional data types besides int, str & float. They include complex float, unsigned integer, unicode string, void, etc.

#Check the data type of an array using 'dtype'
import numpy as np

arr = np.array([13, 27, 19, 6])
print(arr.dtype)

arrStr = np.array(["watermelon", "pineapple", "banana"])
print(arrStr.dtype) # U10 <'U' stands for 'unicode string' in numpy data types>

'''It is possible to define an array's data type using the optional 'dtype' of numpy arrays'''
array = np.array(["16", 27, "13", "twenty-two", 8], dtype = 'U')
print(array.dtype)


import numpy as np
#For types i, f, S, U and u, it is possible to define size as well:

strArr = np.array(["ant", "butterfly", "caterpillar"], dtype = "U4")
print(strArr.dtype) #gives U4, U11 if length is undefined

intArr = np.array([6, 4, 2, 0], dtype = 'i8')
print(intArr.dtype) # 'int64'

#A ValueError is raised if a data type that cannot be converted is present in an array:

'''
arr = np.array(["19", "thirty-five", 6, 15], dtype = "i")
print(arr)
print(arr.dtype)
'''


#array.astype('dtype')
'''Use the 'astype' method to create a copy of an existing array with a specified data type)'''

x = np.array([12, 18, 22, 24, 0])
y = x.astype("U14") #using the symbol (U)
print(y, y.dtype)
z = y.astype("bool") # or using the full name (bool)
print(z, z.dtype)


import numpy as np

#Numpy array Copy Vs. View

"""The 'copy()' method duplicates an existing array in a new one. Both arrays can be changed independently."""
#copy()
x = np.array(["ant", "bee", "wasp"])
xcopy = x.copy()

#changes to the array or copy don't affect the other
x[0] = 17
print(x)
print(xcopy) 

xcopy[1] = 67
print(x)
print(xcopy)

"""The 'view()' method creates a view of an array. Changes made to the original affect the view and vice versa"""
#view()
y = np.array([1, 2, 3, 4])
yview = y.view()

#changes to array or view affect both
yview[0] = 100
print(y)
print(yview)

y[2:] = 3000, 7000
print(y)
print(yview)

import numpy as np
# Check if an array items it's elements
'''this is done using the 'base' function'''
arr = np.array([12, 83, 36, 48, 50])
x = arr.copy()
y = arr.view()


print(arr.base) # None
print(x.base) # None
print(y.base) # prints the elements of arr

'''Numpy array shape'''
#Use the 'shape' attribute to check an array's shape

a = np.array([[1, 4, 5], [29, 83, 0]])

print(a.shape) # '(2, 3)' meaning 2-D (no. of elements in tuple), with 2 items having 3 elements each

#Using ndmin to create 7-D array with 3 and 2 elements in the last two dimensions
d7 = np.array(((77, 82), (95, 32), (2, 3)), ndmin = 7)
print(d7.shape) # gives '(1, 1, 1, 1, 1, 3, 2)'


import numpy as np
'''Numpy reshape arrays'''
#Reshaping can change the number of dimensions in an array or the number of elements in each dimension
a = np.array(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"])

#1-D to 2-D
newa = a.reshape(4, 3)
print(newa)

#A reshape array is a view of the original:
print(newa.base)

#1-D to 3-D
newa2 = a.reshape(2, 2, 3)
print(newa2)

#Reshaping can be done to any shape  as long as elements are equal. Otherwise it gives an error
#newa3 = a.reshape(3, 3) # gives an error

import numpy as np
#Unknown dimension:
'''1 unknown dimension is allowed (indicated by '-1') in the reshape parameters. When given, numpy calculated the correct dimension from what's left'''

arrayz = np.array((10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))

y = arrayz.reshape(-1, 2, 4) # returns a 3-D array of two 2-D arrays each containing 2 lists of 4 elements
print(y, y.ndim)
#only 1 unknown dimension is allowed for a reshape function

#Flattening Arrays
'''This is converting multidimensional arrays to 1 dimension. Use '-1'. '''

z = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

z1d = z.reshape(-1)
print(z1d, z1d.ndim)

#There are other methods for flattening arrays in numpy



import numpy as np
# Numpy array iteration

array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

'''array iteration can be done using a for loop.'''

#1-D array iteration
array1 = array.reshape(-1)
for i in array1:
    print(i) # Loops through all the elements in array1: '1 2 3...'
print(array.shape) #3, 2, 2

#2-D array iteration 
'''in looping through an n-dimensions array, it loops through the next dimension (i.e. 2-D arrays in a 3-D array, 1-D arrays of a 2-D array...)'''

array2 = array.reshape(2, 6)
for i in array2:
    print(i) # Loops through the lists in array 2 ([1, 2...] [7, 8...])

#3-D array iteration

for i in array:
    print(i) #Loops through the 2-D arrays

'''looping through each of the elements requires iterating through each dimension's arrays'''

#iterating the elements of a 3-D array
for a in array: # 2-D arrays
    for b in a: # 1-D arrays
        for c in b: #elements of 1-D arrays
            print(c)

import numpy as np

#Using 'nditer()'

'''Iterating through arrays can also be done using the Numpy 'nditer()' function. This solves some challenges such as iterating through arrays with high dimensionality'''

#Iterate through a 3-D array

array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for element in np.nditer(array):
    print(element)

#Iterate an array as a different data type, use 'op_dtypes'.
for item in np.nditer(array, flags=['buffered'], op_dtypes=['S']):
    print(item)
#    print(item.dtype)

#Iterate through every element, skipping 2 at each step:
for a in np.nditer(array[:, :, ::2]):
    print(" ",a)# ':' is used for array slicing. Maximum step is 2 because each 1-D array has only 2 elements


import numpy as np

#Enumerate
'''Use 'ndenumerate()' to enumerate the items in an array'''

array = np.array([[24, 23], [12, 11]])

for index, element in np.ndenumerate(array):
    print(element, index) #gives '24 (0, 0)'... (It gives separate elements instead of tuple bcos of unpacking [ie x,y = 1,2])

#OR
index = np.ndenumerate(array)

for x in index:
    print(x) #prints tuples: '((0, 0), 24)'...

for x, y in ((1,2),(3,4), (5,6)):
    print(x, y)


import numpy as np

'''Numpy Joining Arrays'''

#arrays are joined in Numpy using the 'concantenate()' function. The axis is specified, otherwise it is taken as 0

a = np.array([1, 2, 3])
b = np.array([6, 5, 4])

abarr = np.concatenate((a, b))
print(abarr)

#Join two 2-D arrays along axis 1 (rows)]

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

xyarray = np.concatenate((x, y), axis = 1)



import numpy as np

#Joining arrays using the 'stack()' function
'''It can be used to join arrays along a new axis, e.g. stack two 1-D arrays to form a 2-D array. Axis is 0 if left unspecified'''

m = np.array([1, 2, 3])
y = np.array([4, 5, 6])

myarray = np.stack((m, y), axis = 1)
print(myarray, myarray.shape) #[[1, 4], [2, 5]...]

arrayed = np.stack((m, y), axis = 0)
print(arrayed, arrayed.shape) #[[1, 2, 3], [4,...]]

#Stack along rows using 'hstack()'

rowarray = np.hstack((m, y))
print(rowarray) #1-D array '[1, 2, 3, 4...]'

#Stack along columns using 'vstack()'

columnarray = np.vstack((m, y))
print(columnarray) #2-D array '[[1, 2, 3], [4...]]'

import numpy as np

#Stack by depth/height using 'dstack()'
heightarr = np.dstack((m, y))
print(heightarr) #'[[1, 4], [2, 5...'


'''Numpy Splitting Arrays'''

import numpy as np

#To split an array, use 'array_split()'
ar1 = np.array([12, 11, 10, 9, 8, 7])

a = np.split(ar1, 3)
print(a) #This divided the array into 3 equal parts

#When the number of elements is not divisible by the sections, the new arrays are adjusted, starting from the last one
x = np.array_split(ar1, 5)
print(x)

#The 'array_split()' method produces an array containing each division as its elements
print(a[0])

#The numpy 'split()' method only works for equal divisions, otherwise it gives an error
b = np.split(ar1, 3)
print(b)
#y = np.split(ar1, 5)
#print(y)

#Splitting n-D arrays
#This works in the same way as 1-D arrays

array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

divided = np.array_split(array2, 4)
print(divided)

# the 4th element is an empty array
print(divided[3])
#other elements are 1-D arrays of 3 0-D arrays each

#Specify the axis to split
hrzntldvd = np.array_split(array2, 3, axis = 1) #this splits it horizontally along rows
print(hrzntldvd)

#spliting along rows can be done using 'hsplit()'
hrzntlsplt = np.hsplit(array2, 3)
print(hrzntlsplt)

#other options are 'vsplit()' and 'dsplit()' for splitging vertically and by depth.


'''Numpy Search Array'''

#The function 'where()' is used to search an array for a specified value
array = np.array([[[6, 74, 3], [12, 18, 7]], [[13, 8, 6], [34, 6, 8]]])
print(np.where(array == 6))


import numpy as np

'''Numpy Search Array'''

#The function 'where()' is used to search an array for a specified value
array = np.array([[[6, 74, 3], [12, 18, 7]], [[13.5, 8, 6], [34, 6, 12]]])

print(np.where(array == 6))
# a tuple containing the index locations of 6 (as arrays) 

#Find Odd numbers
print(array%2 == 1)

#Find Even numbers
print(array%2 == 0)

#Find numbers that have 1.5 remainder when divided by 3
print(array%3 == 1.5)


array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#Find numbers divisible by 3
print(array2%3 == 0)

'''Numpy Seach Arrays'''
import numpy as np

arr = np.array([6, 7, 8, 9])

#where() is used to find all indexes where am element is present
a = np.where(arr == 8)

print(a)

#'searchsorted()'
x = np.searchsorted(arr, 8.5)

print(x)

y = np.searchsorted(arr, 8, side = 'right')

print(y)

z = np.searchsorted(np.array([3, 5, 7, 9]), [8, 6, 4], side = 'right')

print(z)

'''Numpy Sorting Arrays'''

import numpy as np

array = np.array([7, 9, 6, 8, 10,])

x = np.sort(array)
print(x) #'x' is a copy of 'array'

b = np.array(('ant', 'bee', 'catepillar', 'dragonfly'))

y = np.sort(b)
print(b)

c = np.array([True, False, False, True])

z = np.sort(c)
print(z)

#Sorting 2D arrays

arrayed = np.array([[6, 7, 5],[2, 0, 1]])

print(np.sort(arrayed)) #only sorts the elements of the 1-D arrays

'''Numpy Filter Array'''
import numpy as np

#Filtering an array is done using a list of Booleans to create an array by excluding some elements of an existing array:-
a = np.array([1,2,3,4,5])

print(a[[True, False, False, True, True]])

#Using a condition to create a lost:-
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filter = []

for i in array:
    if i%2 == 0:
        filter.append(True)
    else:
        filter.append(False)
print(filter)

x = array[filter]
print(x)


#Create filter directly from an array
x = np.array([13, 11, 9, 7, 5, 3])

filter_x = x > 7

filteredx = x[filter_x]

print(filter_x)
print(filteredx)


'''Numpy Random Numbers'''

from numpy import random

#'randint()' random number maximum of 100
a = random.randint(100)
print(a)

#'rand()' for random decimal between 0 and 1
b = random.rand()
print(b)

#Create random arrays using rand() and randint()

#use 'size' parameter for randint()
x = random.randint(20, size=(10))
print(x)
y = random.randint(50, size=(2,5))
print(y)

#define shape of array in rand()
c = random.rand(3,3,2)
print(c)

#random numbers from existing arrays: 'choice()'
items = [12, 15, 18, 21, 24, 27]

m = random.choice(items)
print(m)

n = random.choice(items, size = (5, 2, 2))
print(n)


'''Random Data Distribution'''

from numpy import random

#a random distribution is a set of numbers that follows a certain probability distribution (the likelihood that a number will occur{?})

x = random.choice([11, 21, 12, 24], p = [0.25, 0.6, 0.15, 0], size = (20))
print(x)



