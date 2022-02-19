import pandas as pd
import matplotlib.pyplot as plt


airports = pd.read_csv('csv/airports.csv')


airports['iso_country'][pd.isnull(airports['continent'])].unique()


airports['continent'][pd.isnull(airports['continent'])]='NA' # With Warnning


airports.loc[pd.isnull(airports['continent']),'continent']='NA' # No Warnnig



airports['type'].value_counts().plot(kind='bar',figsize=(10,10))
plt.xlabel('airport Types')
plt.ylabel('Count')
plt.show()


airports['type'].value_counts().plot(kind='pie',figsize=(8,8))
plt.show()


airports.groupby(['type','continent']).size()


airports.groupby(['type','continent']).size().unstack().plot(kind='bar',stacked=True,figsize=(7,7))
plt.savefig('plot_saved.png') # Save Plot module to png
plt.show()


