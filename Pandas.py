'''*********************************
            Pandas Tutorial
**********************************'''

# Pandas🐼 is a python library for
# handling datasets. It enables 
# cleaning, analyzing and 
# manipulation of datasets

import pandas

dataset = {
  'cars': ["Fiat", "Aston Martin", "Toyota"],
  'sightings': [7, 4, 18]
}

new_table = pandas.DataFrame(dataset)

print(new_table)

'''Pandas is usually imported as "pd".'''

import pandas as pd

data_table = pd.DataFrame(dataset)
print(data_table, "\n\n")

# Pandas Version

print(pd.__version__)


'''Pandas Series'''

# A series is a 1-D array of data
# it is like a single column from
# a table

import pandas as pd

column = [18, 12, 27]

a = pd.Series(column)
print(a)

# By default, a column is labelled 
# by number indexes, which can be 
# used to access its elements

print(a[0]) #18

# Specify column labels using the 
# index parameter

grades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = pd.Series(grades, 
              index = ["A", "B", "B", "C", 
                       "C", "C", "D", "E", "F"])
print(b)

# Access elements 
print(b["A"])
print(b["C"])
print(b["E":])

# Use key-value objects as a series
# the keys will be indexes of the 
# value elements

speed = {
  "Mitsubishi": 320, 
  "Hyundai": 290,
  "Toyota": 270,
  "Audi": 350
}

x = pd.Series(speed)
print(x)

# Use index to specify which elements
# from a key-value object to include
# in the series

y = pd.Series(speed, index = [
  "Mitsubishi", "Audi"])
print(y)

# Dataframes are like tables while 
# series are like columns on tables

cars = {
  "brand": ["Toyota", "Hyundai", 
            "Audi", "Mercedes-Benz"],
  "count": [18, 7, 4, 11]
}

passing_cars = pd.DataFrame(cars)

print(passing_cars)


'''Pandas DataFrame'''

# An array is a 2-D data structure, 
# A table of columns and rows

import pandas as pd

chess_csv = {
  "master": ["Poliakoff", 
              "Broderick", "Hamada", 
              "Santanu", "Maxwell", 
             "Lee"], 
  "rank": [327, 359, 372, 337, 340, 
          314],
  "age": [37, 42, 29, 34, 54, 12]
}

df = pd.DataFrame(chess_csv)

print(df)

# Locate a specific row with 'loc'

oldest = df.loc[4]
print(oldest) #result is a pd series

# Locate more than 1 row

print(df.loc[[0, 1, 2]])#pd dataframe


# Named Indexes: create labels for 
# each row by adding a list of indexes

df2 = pd.DataFrame(chess_csv, 
                   index = [
                     "1st player", 
                     "2nd player",
                     "3rd player",
                     "4th player",
                     "5th player",
                     "6th player"])

print(df2)

# Locate named indexes 

print(df2.loc["6th player"])

#Load Files into A Dataframe

# CSV file

data = pd.read_csv("data.csv")
print(data)


'''Pandas Read CSV'''

import pandas as pd

df = pd.read_csv("data.csv")

#Print a truncated version
print(df)

#Print the entire dataframe
print(df.to_string())

#Print first 5 rows
print(df.head())



'''Pandas Read JSON'''

import pandas as pd

df = pd.read_json("data.json")

print(df.to_string)

#JSON objects have the same format as python dict
#dictionaries can be loaded directly into dataframes


'''Pandas Analyze Dataframe'''

import pandas as pd

data = {
  "brand": {
    1:"Toyota", 2:"Honda", 3:"Tesla", 
    4:"Mitsubishi", 5:"Audi", 6:"Nissan", 
    7:"Opel", 8:"Geely", 9:"Vibe", 10:"Ford", 
    11:"Talon"
  },
  "counted": {
    10:42, 2:23, 3:11, 4:17, 5:15, 6:34, 7:9, 8:6, 9:13, 
    10:16, 11:14
  }
}

df = pd.DataFrame(data)

# head(): this method returns the 
# header and a specified number of
# rows from the top (default 5)

print(df.head(10))

print("\n\n", df.head(), "\n\n")


#tail: gives the header and rows from 
#the bottom (default 5)

print(df.tail())

#info: gives information about the 
#dataframe

print(df.info())



'''Pandas Clean Dataframes'''

import pandas as pd

df = pd.read_csv("data.csv")

df.head()

#Remove rows with nan (empty) cells

df_copy = df.dropna()

print(df_copy.to_string()) # this creates a new dataframe. 

#use inplace = True to change the original dataframe

'''
df.dropna(inplace = True)

print(df.to_string())
'''


# Fill empty cells

df_filled = df.fillna(60) # use inplace = True to change original

print(df_filled)

#Fill empty cells for specified columns 

df_dur = df["Duration"].fillna(60)

print(df_dur) # result is series. Use inplace = True to change the original dataframe
import pandas as pd

df = pd.read_csv("data.csv")

# Fill null values with mean, median & mode

#mean
df1 = df.copy()

mean = df1["Calories"].mean()

df1["Calories"].fillna(mean, inplace = True)

print(df1)

#median

df2 = df.copy()

median = df2["Calories"].median()
print(median)

#mode

df3 = df.copy()

m = df3["Calories"].mode()[0]

df3["Calories"].fillna(m, inplace = True)

print(df3)


'''Pandas clean wrong format data'''

import pandas as pd

# There are 2 options: 
# remove the rows that contain wrong
# format data
# OR
# Convert data to correct format

#Convert data to correct format
#using Pandas to_datetime method


df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["Date"])

print(df)

#Remove NaT value using dropna 

df.dropna(subset = ["Date"], inplace = True) # only drop rows with na values date

print(df)


'''Pandas Fixing wrong data'''

# Sometimes data the wrong data may be entered. To correct it one can

# Replace the data:-

#For a small dataset
import pandas as pd

df = pd.read_csv("data.csv")

#print(df)

df.loc[7, "Duration"] = 45
print(df.to_string())


# For large datasets conditions can be used

# Replace wrong data 

for row in df.index:
 if df.loc[row, "Duration"] > 120:

  df.loc[row, "Duration"] = 120


print(df.to_string)

# or the rows can be removed

for y in df.index:
 if df.loc[y, "Duration"] > 60:
  df.drop(y, inplace = True)

print(df)


'''Pandas remove duplicates'''

import pandas as pd

df = pd.read_csv("data.csv")

#Use the duplicated method

print(df.duplicated()) # True at 12

# Use the drop_duplicate method to remove duplicates

df.drop_duplicates(inplace = True)

print(df)



'''Pandas Data Correlations'''

import pandas as pd

#Use the corr function to check correlations between columns

df = pd.read_csv("data.csv")

correlation = df.corr()

print(correlation)



'''Pandas Plotting'''

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("data.csv")

df.plot()

plt.show()

# Use a scatterplot

df.plot(kind = "scatter", x = 'Duration', y = 'Calories')

plt.show()

#Visualize a pair with little correlation

df.plot(kind = "scatter", x = "Duration", y = "Maxpulse")

plt.show()

# Use a histogram to visualize frequency

df["Duration"].plot(kind = "hist")

plt.show()
