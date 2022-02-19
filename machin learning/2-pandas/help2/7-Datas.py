import pandas as pd


df=pd.read_csv('csv/countries.csv')
print(df)


print(df['name'])



print(type(df['name']))


print(df[['name']])


print(type(df[['name']]))


print(df[['name','id']])


print(df.loc[1:10,['name','id']])


print(df['id'].value_counts())


print(df['id'].unique())


x=[1,3,5,8,56,'hello',45,12]
sr=pd.Series(x,index=['a','b','c','d','e','f','g','h'])

print(sr)

print(sr['e'])