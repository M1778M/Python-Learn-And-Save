import pandas as pd
import numpy as np

myArr = np.array([[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]])

myDf = pd.DataFrame(myArr,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])

print(myDf)

print()

mydict = {'col1':[1,2,3,4],'col2':[5,6,7,8],'col3':[9,10,11,12],'col4':[13,14,15,16]}

myDf2 = pd.DataFrame(mydict,index=['row1','row2','row3','row4'],columns=['col1','col2','col3','col4'])

print(myDf2)


