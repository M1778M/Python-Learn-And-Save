import numpy as np
import pandas as pd
import json
myDict = {'C1':[1,2,3,4],'C2':[5,6,7,8],'C3':[9,10,11,12],'C4':[13,14,15,16]}

myDf = pd.DataFrame(myDict,index=['Row1','Row2','Row3','Row4'],columns=['C1','C2','C3','C4'])

myDf.C1=['{:.2f}'.format(x) for x in myDf.iloc[:,0]]

print(myDf)

print()

myDf['C2']=myDf['C2'].apply(lambda x:'{:.2f}'.format(x))

print(myDf)

print()

myDf.sort_index(axis=0,ascending=False)
print(myDf)
print()


myDf.sort_values(by='C4',ascending=False)

print(myDf)

print()

print(myDf.head(2))
print(myDf.head())

print()

print(myDf.tail())
print(myDf.tail(2))

print()



data = pd.read_csv('D:\\Downloads\\test.csv')

print(data)
