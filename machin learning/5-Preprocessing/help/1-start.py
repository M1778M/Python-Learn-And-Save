import numpy as np
import pandas as pd
from sklearn import preprocessing as ps


countries = pd.read_csv('D:\\Downloads\\example-countries.csv',header=0)

print(countries)

countries.rename(columns={"Country (en)" : "Country"},inplace=True)
print(countries)


