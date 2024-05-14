# ---q1---
#In the editor, write code to see if True equals False.
#Write Python code to check if -5 * 15 is not equal to 75.
#Ask Python whether the strings "pyscript" and "PyScript" are equal.
#What happens if you compare booleans and integers? Write code to see if True and 1 are equal.

#Comparison of booleans
print(True == False)

#Comparison of integers
print(-5*15 != 75)

#Comparison of strings
print("pyscript" == "PyScript")

#Comparison of booleans and integers
print(True == 25)

# ---q2---
# Define x as -3*6
# Check whether x is greater than or equal to -10.
# Define y as "test".
# Check whether "test" is less than or equal to "y".
# Check whether True is greater than False.

x = -3*6
print(x>=-10)

y = 'test'

print("test"<=y)

print(True>False)

# ---q3---
#Create two numpy arrays called my_house and your_house from the table below that contains the areas for the kitchen,\
#living room, bedroom and bathroom.
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# Which areas in my_house are greater than or equal to 18?
# You can also compare two Numpy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
# Make sure to wrap both commands in a print() statement so that you can inspect the output!

# my_house greater than or equal to 18
print(my_house>=18)
# my_house less than your_house
print(my_house < your_house)


# ---q4---

# Extract the areas of kitchen from the my_house and your_house and assign them to my_kitchen and your_kitchen.
# Check whether;
# my_kitchen is bigger than 10 and smaller than 18.
# my_kitchen is smaller than 14 or bigger than 17.
# Double the area of my_kitchen is smaller than triple the area of your_kitchen.
 
#define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen < 3*your_kitchen)

# ---q5---
# Some weather related variables are stored in the weather_data.csv.
# Import the data with the read_csv() function.
# Print first few and last lines of the code and look at the information of the variables.
# Do you think the variable Date is imported correctly?
# This time import the data with the following code.
import pandas as pd
df = pd.read_csv(r"C:\Users\efeha\OneDrive\Masaüstü\weather_data.csv")
print(df.head())
print(df.tail())
df.info()

wth = pd.read_csv(r"C:\Users\efeha\OneDrive\Masaüstü\weather_data.csv",parse_dates = ["Date"] )
# parse_dates argument provides a way to import the dates.
# Print first few and last lines of the code and look at the information of the variables.
# Did anything changed?
# Now use describe() on the data and find some descriptive statistics.
# Find the average temperature bu using numpy and confirm the finding above.
# Find how many measurements are there above average temperature?
print(wth.head())
print(wth.tail())
wth.info()
wth.describe()
import numpy as np
mena_temp = wth['Temperature'].mean()
print(mena_temp)
print(wth[wth['Temperature']>mena_temp].shape[0])

# ---q6---
# Another dataset called spotify.csv is provided to you.
# This dataset contains information about songs.
# First set number of columns to be seen in the output to a reasonable number so that all the columns can be seen in the output.
# Import the dataset to a dataframe called spotify.
# Look at the first 4 and last 8 rows of the dataset.
# Determine how many rows and columns exists in the data.
# Remove the duplicate rows and check if any rows are removed from the data.
# Rename the column artist as singer.
# Check if any missing values exist in the data.
# Find the top 10 singer with the highest number of songs in the dataset.
# Extract all the songs performed by ‘Michael Jackson’.
# Extract all the songs performed by ‘Drake’.
# Extract all the songs performed by either ‘Michael Jackson’, ‘Drake’, or ‘Katy Perry’.
# Extract all the songs performed by either ‘Michael Jackson’, ‘Drake’, or ‘Katy Perry’ and has a tempo value over 140.
# Compare average tempo for songs performed by ‘Michael Jackson’ and ‘Drake’.
import pandas as pd
data = pd .read_csv(r"C:\Users\efeha\OneDrive\Masaüstü\spotify.csv",index_col=0)
print(data.head())
print(data.info())
data.describe()
pd.options.display.max_columns = 99
spotify = pd.DataFrame(data)
print(spotify.head(4))
print(spotify.tail(8))
print(spotify.shape)

spotify.drop_duplicates(inplace=True)
print(spotify.shape)
# Number of rows are 2012, 5 duplicates are removed

spotify.rename(columns = {'artist':'singer'}, inplace = True)
print(spotify.head(5))
print(spotify.isnull().sum())
print(spotify['singer'].value_counts().head(10))

print(spotify[spotify['singer']=='Michael Jackson'])
print(spotify[spotify['singer']=='Drake'])

print(spotify[(spotify['singer']=='Michael Jackson')|(spotify['singer']=='Drake')|(spotify['singer']=='Katy Perry')])

    
print(spotify[spotify['singer'].isin(['Michael Jackson','Drake','Katy Perry'])])  
    
print(spotify[(spotify['singer'].isin(['Michael Jackson','Drake','Katy Perry']))&(spotify['tempo']>140)])  

print(spotify[spotify['singer']=='Michael Jackson']['tempo'].mean())
print(spotify[spotify['singer']=='Drake']['tempo'].mean())