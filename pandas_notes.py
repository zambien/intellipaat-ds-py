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

print_header("Outer Merge")

print (df1.merge(df2, on='Player', how='outer'))

## Note, difference between join and merge:
##   - Merge works on the attributes in a Data Frame
##   - Join works on an index in a data frame

print_header("Join Operation")

player = ['Player1','Player2','Player3']
point = [8,9,6]
title = ['Game1','Game2','Game3']

df3 = pd.DataFrame({'Player':player, 'Points':point, 'Title':title}, index = ['L1', 'L2', 'L3'])

print (df3)

player = ['Player1','Player5','Player6']
power = ['punch','kick','elbow']
title = ['Game1','Game5','Game6']

df4 = pd.DataFrame({'Players':player, 'Power':power, 'Titles':title}, index = ['L2', 'L3', 'L4'])

print (df4)

print_header("Inner Join")

print(df3.join(df4, how='inner'))

print_header("Left Join")

print(df3.join(df4, how='left'))

print_header("Right Join")

print(df3.join(df4, how='right'))

print_header("Outer Join")

print(df3.join(df4, how='outer'))

print_header("Concatenate two data frames")

print(pd.concat([df3,df4]))

print_header("Importing and Analyzing Datasets")

cars = pd.read_csv("mtcars2.csv")

print (cars)

print_header("pd.read_csv(\"mtcars2.csv\") is a data frame:")
print(type(cars))

print_header("first 5 records")
print(cars.head())

print_header("first 10 records")
print(cars.head(10))

print_header("last 5 records")
print(cars.tail())

print_header("last 10 records")
print(cars.tail(10))

print_header("shape - what is the shape of the data?")
print("shape is rows: " + str(cars.shape[0]) + ", columns: " + str(cars.shape[0]))

print(cars.info(null_counts=True))

print_header("cars.mean")
print(cars.mean())

print_header("cars.median")
print(cars.median())

print_header("cars.std - standard deviation")
print(cars.std())
 
print_header("cars.max - max values")
print(cars.max())

print_header("cars.min - min values")
print(cars.min())

print_header("cars.count - non-null values")
print(cars.count())

print_header("cars.describe - summary of all descriptor statistics")
print(cars.describe())

print_header("Data Cleansing")

print_header("rename column")
cars = cars.rename(columns={'Unnamed: 1':'model'})
print(cars)

print_header("fill in null values with the mean of the column")
cars.qsec = cars.qsec.fillna(cars.qsec.mean())
print(cars)

print_header("Drop unwanted columns")
cars = cars.drop(columns=['S.No'])
print(cars)

print_header("Find correlation matrix")
df = cars[['mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].corr()
print(df)

print_header("Change the data type")
cars.mpg = cars.mpg.astype(float)
print (cars.info(null_counts=True))

print_header("Find correlation matrix after correcting mpg from string to float")
df = cars[['mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].corr()
print(df) 

print_header("Manipulating the data set")

print_header("view hp column only")
print(cars.iloc[:,4])

print_header("view first 5 rows of hp column only")
print(cars.iloc[0:5,4])

print_header("view all rows and columns")
print(cars.iloc[:,:])

print_header("view subset of rows and columns")
print(cars.iloc[6:,4:])

print_header("view by named column, not loc (location) instead of iloc (index location)")
print(cars.loc[:,"mpg"])

print_header("loc up to row 6 and column range")
print(cars.loc[:6,"mpg":"qsec"])

print_header("set all values of column am to 1")
cars['am']=1
print(cars)

print_header("double up records in 'am' using lambda function")
f = lambda x: x*2
cars['am'] = cars['am'].apply(f)
print(cars)

print_header("sorting cyl column ascending")
print(cars.sort_values(by='cyl'))

print_header("sorting cyl column descending")
print(cars.sort_values(by='cyl', ascending=False))

print_header("filter records to cyl > 6")
print(cars['cyl'] > 6)

print_header("print records with cyl > 6")
filter1 = cars['cyl'] > 6
print(cars[filter1])

print_header("print records with cyl > 6 and more than 300 hp")
filter2 = (cars['cyl'] > 6) & (cars['hp'] > 300)
print (cars[filter2])