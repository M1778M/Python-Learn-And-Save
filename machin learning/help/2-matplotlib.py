import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix

hosting = pd.read_csv('hosting.csv',header=0,sep=',')

train_set,test_set = train_test_split(hosting,test_size=0.2,random_state=42)

train_set.shape

train_set.head()

data = train_set.copy()

data.head()


data = train_set.copy()

data.plot(kind="scatter",x="longitude",y="latitude",s=data["population"]/30,label="population",c=data["median_house_value"],cmap=plt.get_cmap('jet'),figsize=(10,7),alpha=0.7)

print(data.shape)

# corr Data
corr_matrix = data.corr()

corr_matrix['median_house_value'].sort_values(ascending=False)

# Plot
ft = ['median_house_value','median_income','total_rooms','housing_median_age']

scatter_matrix(data[ft])

plt.show()


# Plot
data.plot(kind="scatter",x="median_income",y="median_house_value",figsize=(10,7),alpha=0.7)
plt.show()


# Append New Datas
data["total_rooms_per_households"] = data["total_rooms"]/data["households"]#New Data
data["total_bedrooms_per_total_rooms"] = data["total_bedrooms"]/data["total_rooms"]
data["population_per_households"] = data["population"]/data["households"]

print(data.head())


corr_matrix = data.corr()

corr_matrix['median_house_value'].sort_values(ascending=False)
