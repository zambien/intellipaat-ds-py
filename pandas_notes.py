import pandas as pd

def print_header(header):
    print ("\n" + header + "\n")


print_header("Series Object in Pandas")

data = [1, 2, 3, 4]
series1 = pd.Series(data)

print(series1)

print(type(series1))

print_header("Changing the Index of a Series Object")

series1 = pd.Series(data, index=['a','b','c','d'])
print(series1)

print_header("How to create a dataframe using a list")

data = [1,2,3,4,5]
df = pd.DataFrame(data)

print (df)

print_header("Creating a datafram using dictionary")

dictionary = {'fruit':['apple','banana','mango'],'count':[10,20,15]}

df = pd.DataFrame(dictionary)

print (df)

print_header("Creating a dataframe using a series")

series = pd.Series([6,12], index=['a','b'])

df = pd.DataFrame(series)

print (df)

print_header("Create dataframe using numpy array")

import numpy as np

numpyarray = np.array([[50000,60000],['John','James']])

df = pd.DataFrame({'name':numpyarray[1],'salary':numpyarray[0]})

print (df)

print_header("Perform a merge operation")

player = ['Player1','Player2','Player3']
point = [8,9,6]
title = ['Game1','Game2','Game3']

df1 = pd.DataFrame({'Player':player, 'Points':point, 'Title':title})

print (df1)

player = ['Player1','Player5','Player6']
power = ['punch','kick','elbow']
title = ['Game1','Game5','Game6']

df2 = pd.DataFrame({'Player':player, 'Power':power, 'Title':title})

print (df2)

print_header("Inner Merge (default with no how definition)")

print (df1.merge(df2, on='Player', how='inner'))

print_header("Left Merge")

print (df1.merge(df2, on='Player', how='left'))

print_header("Right Merge")

print (df1.merge(df2, on='Player', how='right'))