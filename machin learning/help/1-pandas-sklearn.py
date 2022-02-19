# تحلیل داده
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
hosting = pd.read_csv('hosting.csv')

# Read CSV
print(hosting.head())

print(hosting.tail(5))

print(hosting[2:5])

hosting = pd.read_csv('hosting.csv', header=0, sep=',', names=['longitude','latitude','housing_median_age','total_rooms','total_bedrooms','population','households','median_income','median_house_value','ocean_proximity'])


print(hosting.shape)

print(hosting.info())

print(hosting.columns)

print(hosting['ocean_proximity'])

print(hosting['ocean_proximity'].unique())

print(hosting['ocean_proximity'].value_counts())

print(hosting[hosting['ocean_proximity']=='ISLAND'])

print(hosting['population'][hosting['ocean_proximity']=='ISLAND'])

print(hosting[['population','latitude']][hosting['ocean_proximity']=='ISLAND'])

print(hosting.describe())


# END Read CSV and Info

#--------------------------------------------

# Show Data

hosting.hist(bins=50,figsize=(20,15))
plt.show()


# End Show Data


# Use sklearn

train_set,test_set = tts(hosting,test_size=0.2,random_state = 42)

print(train_set.shape)


# End Use
