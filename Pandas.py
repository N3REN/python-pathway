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
