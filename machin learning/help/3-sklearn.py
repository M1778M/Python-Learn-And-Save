import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
import numpy as np

hosting = pd.read_csv('hosting.csv',header=0,sep=',')

train_set, test_set = train_test_split(hosting,test_size=0.2,random_state=2)
print(train_set.shape)
print(train_set.head())


data =  train_set.copy()
data.plot(kind='scatter',x='longitude',y='latitude',
         s=data['population']/30,label='population',
         c=data['median_house_value'],cmap=plt.get_cmap('jet'),
         figsize=(10,7),alpha=0.2)

