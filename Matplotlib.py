"""Python Modules"""

'''Matplotlib'''

import matplotlib

print(matplotlib.__version__)

#most matplotlib utilities are in the pyplot submodule:
import matplotlib.pyplot as plt
#OR 'from matplotlib import pyplot as plt'

#use pyplot:
import numpy as np
x_axis = np.array([0, 10])
y_axis = np.array([0, 10])

plt.plot(x_axis, y_axis)

plt.show()

'''Plot'''
#plot is used for drawing points in a diagram,
# draws a line to connect points by default,
# and takes 2 parameters, an array containing
# the points on x axis and an array containing
# the points on y axis. 

X = np.array([1,8])
Y = np.array([3,10])

plt.plot(X, Y)
plt.show()


#To show only markers:

X = np.array((2, 37))
Y = np.array((5, 40))

plt.plot(X, Y, "o") #Use 'p' for 'pentagon' and 'x' for 'crosses'
plt.show()


#Plot Multiple points
X = np.array([4, 1, 7, 23, 30])
Y = np.array([1, 13, 27, 21, 35])

plt.plot(X, Y)
plt.show

#Default x-points

#leaving points on the x-axis unspecified
# leaves the default x-values which are
# (1, 2, 3,..) to as many points as are
# specified for y-axis:
plt.plot(np.array((5, 8, 4, 5, 7)))
plt.show()

#Markers

#To emphasize each point with a marker,
# use the keyword argument 'marker':
Y = np.array([7, 11, 5, 13])
#plt.plot(Y, marker = "p")#pentagon
plt.show()

plt.plot(Y, marker = ",")#star
plt.show()

#Format string 'fmt':
#is shortcut used to specify marker shape as well as color

plt.plot(Y, "o-.r")
plt.show()


# Marker size, face and edge colour
import matplotlib.pyplot as plt

y = [7, 2, 9, 1, 13, 3, 21]

plt.plot(y, 
         marker = '*', 
         markersize = 20, 
         markerfacecolor = '#ff18b1',
         markeredgecolor = 'b', 
         linestyle = '-',
         color = 'b'
         )

plt.show()

# shortcuts: markersize=ms, 
# markerfacecolor=mfc, 
# markeredgecolor=mec

plt.plot([5, 3, 7, 4, 9], marker = 'o',
         ms = 15, mfc = 'g', mec = 'r', 
        ls = '-.', c = 'm')
plt.show()



'''Matplotlib line'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([4, 16, 3, 12, 18])
# specify line style using 
# 'linestyle' or 'ls'. Use 'color' or
# 'c' for line color
# specify line width with 'linewidth'
# or 'lw'

plt.plot(y, linestyle = 'dashed', linewidth = 5.50, 
         c = 'g', marker = 'H', ms = 20)

plt.show()

# To plot multiple lines: 
x = [1, 2, 3, 4]
y2 = [2, 8, 3, 9]
y3 = [3, 9, 4, 11]

plt.plot(y2, ls = ':', lw = 6, c = 'b', ms = 16) 
plt.plot(y3, ls = '-.', lw = 4, c = 'r', ms = 10) 

#plt.show()

# OR

plt.plot(x, y2, x, y3)

plt.show()



'''Matplotlib Labels & Title'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([10.2, 23.7, 31.0, 38.4, 
             42.7, 48.9, 53.2])
y = np.array([5400, 4900, 4200, 3500, 
             2800, 2100, 1400])

font1 = {'family': 'sans', 'size': 20, 
        'color': 'indigo'}
font2 = {'family': 'serif', 'size': 15, 
        'color': 'violet'}

plt.plot(x, y, ls = '-.', lw = 5, 
         c = 'blue', mfc = 'y', 
         mec = 'b', ms = 12, 
        marker = 'H')

plt.xlabel("Velocity (m/s)", fontdict = font2)
plt.ylabel("Elevation (meters)", fontdict = font2) 
plt.title("Skydive Log", fontdict = font1, loc = 'left')

plt.show()


'''Matplotlib Grid'''
import matplotlib.pyplot as plt
import numpy as np

# add gridlines to plot
# axis can be 'x', 'y' or 'both'
# specify color, linestyle & 
# linewidth

plt.grid(axis = 'both', color = 'green', 
        ls = '--', lw = 0.5)

plt.show()




'''Matplotlib Subplots'''

# subplots enable drawing more than
# one plot in one figure

import matplotlib.pyplot as plt 
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 9, 6, 7, 2]

plt.subplot(1, 2, 1)
plt.plot(x, y)

x2 = [2, 5, 3, 7, 10]
y2 = [1, 2, 3, 4, 5]

plt.subplot(1, 2, 2)
plt.plot(x2, y2)

plt.show()


# in subplot(a, b, c), a: number of 
# rows, b: number of columns, 
# c: position of current subplot

plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.plot(x2, y2)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# add title to each subplot using
# plt.title()
# add title to the whole plot using
# plt.suptitle()

x = [3,6,6,7]
y = [3,5,3,2]
plt.subplot(2,3,1)
plt.plot(x,y)

x = [5,2,6,0]
y = [6,1,7,9]
plt.subplot(2,3,2)
plt.plot(x,y)

x = [6,4,1,0]
y = [4,2,3,7]
plt.subplot(2,3,3)
plt.plot(x,y)

x = [5,2,1,4]
y = [6,5,8,2]
plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("Fourth")

x = [5,3,8,7]
y = [2,3,4,1]
plt.subplot(2,3,5)
plt.plot(x,y)
plt.title("Fifth")

x = [5,6,4,0]
y = [12,17,2,9]
plt.subplot(2,3,6)
plt.plot(x,y)
plt.title("Sixth")

plt.subplots_adjust(hspace=0.5)
plt.suptitle("Six Plots")
plt.show()



'''Matplotlib Scatter'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([7,2,17,6,5,12,14,8,9,
              1,3,18,3])
y = np.array([89,113,82,102,94,92,79,
              87,84,102,90,76,99])

plt.scatter(x, y, color = "#E52B50")

colormap = np.array(["#B8860B","#B31B1B","#FF3800","#0047AB","#7B3F00","#E68FAC","#B0BF1A","#E52B50","#007AA5","#6F4E37","#7FFF00"])

x1 = np.array([16,1,11,1,13,4,9,3,10,
               2,12])
y1 = np.array([88,112,94,98,77,92,79,
               102,81,90,76])

plt.scatter(x1, y1, c = colormap)

plt.show()


# Use an inbuilt colormap
colors = [10,20,25,35,40,45,50,60,
          70,75,80,90,100]

plt.scatter(x, y, c = colors, cmap = 'Spectral')
plt.colorbar()

plt.show()

# Make an array of numbers to change 
# dot sizes using s = size_array
# Use 'alpha' argument to set dot transperency


x = np.random.randint(50, size = (100))
y = np.random.randint(50, size = (100))

sizes = np.random.randint(1000, size = (100))
colours = np.random.randint(100, size = (100))

plt.scatter(x, y, c = colours, cmap = 'Spectral', s = sizes, alpha = 0.5)
#plt.colorbar()
plt.show()



'''Matplotlib Bars'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Uno","Dos","Tres", 
              "Cuarto"])
y = np.array([10,20,30,40])

plt.bar(x, y)
plt.show()

# Use barh() for horizontal bars
plt.barh(x, y)
plt.show()

# Set bar colors
plt.bar(x, y, color = '#8C92AC')
plt.show()

# Set bar width (vertical) or height
# (horizontal)

plt.bar(x, y, color='aquamarine', width=0.3)
plt.show()

plt.barh(x, y, color = 'green', 
         height = 0.5)
plt.show()



'''Matplotlib Histograms'''

# histograms are used to show frequeny
# distributions

import matplotlib.pyplot as plt
from numpy import random as r

normal = r.normal(100, 25, size=(1000))
#print(normal)
plt.hist(normal)

plt.show()



'''Matplotlib Pie Charts'''

import numpy as np

a = np.array([14, 24, 19, 38, 10])
print(a/sum(a)) # ratios of pie segments

plt.pie(a) 

# add label using 'labels'
label = np.array(["Aston Martin",
                  "Ford","Audi",
                  "Geely", "BMW"])

# by default the pie starts on the 
# right and continues counterclockwise
# change default angle using 'startangle'

angle = 270 # start from bottom

# use 'explode' to make paricular
# segments stand out

stdout = [0.0, 0, 0, 0.1, 0.05]

# segments stand out
# Use shadow = True to add shadow

# Choose colors for the segment with
# colors = array_of_colors
array_of_colors = np.array(["#7FFF00",
                            "#0047AB",
                            "#FF3800",
                            "#B31B1B",
                            "#8C92AC"])

plt.pie(a, labels = label, 
        startangle = angle, 
        explode = stdout, 
        shadow = True,
       colors = array_of_colors)

# Add a legend to the pie chart
plt.legend(title = "Cars")

plt.show()

