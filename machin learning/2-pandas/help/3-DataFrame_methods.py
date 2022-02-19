import numpy as np
import pandas as pd


myDict = {'C1':[1,2,3,4],'C2':[5,6,7,8],'C3':[9,10,11,12],'C4':[13,14,15,16]}


myDf = pd.DataFrame(myDict,index=['Row1','Row2','Row3','Row4'],columns=['C1','C2','C3','C4'])

print(myDf.index)
print(myDf.columns)
print()
print(myDf.values)
print()

print(myDf.loc['Row1']['C2']) # To Find By RowName and Col Name

print(myDf.iloc[0][1]) # To Find By Id

print()

myDf['C5'] = [17,18,19,20]

print(myDf)

myDf.loc[['Row1','Row2'],'C1']=0

print()
print(myDf)
print()

myDf.reset_index(drop=True,inplace=True) # inplace = برای ست کردن و زخیره در دیتا و بدون نیاز به تعریف مای دی اف دوباره

print(myDf)

myDf.drop('C5',axis=1,inplace=True)

print(myDf)

print()

myDf.rename(columns={'C4':'COL4'},inplace=True)
print(myDf)

print()

myDf.replace(0,1) # تبدیل تمام 0 ها به 1


