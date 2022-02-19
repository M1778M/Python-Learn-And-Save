import pandas as pd
import numpy as np


df = pd.read_csv('data.csv')

print(df)


print(df.isnull())




print(df.isnull().sum().sum()) # or sum()



df = pd.read_csv('data.csv',na_values=['\'NaN\'','na'])
print(df)


print(df.loc[1,'age'])




i=0
for age in df['age']:
    try:
        int(age)
    except:
        df.loc[i,'age']=np.nan
        pass
    i+=1
    
print(df)



df.loc[(df['gender']!='m') & (df['gender']!='f'),'gender']=np.nan


print(df)
