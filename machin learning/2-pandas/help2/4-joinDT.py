import pandas as pd


data = {'id':[1,2,3,4,5],'gens':['m','f','m','m','f'],'age':[15,18,32,23,65]}
df=pd.DataFrame(data)
print(df)


data2 = {'id':[1,2,3,4,5],'gens':['m','f','m','m','f'],'age':[15,18,32,23,65],'job':['dv','dv','dv','NHJ','wdv']}
df2=pd.DataFrame(data2)
print(df2)



print(pd.merge(df,df2,left_on='id',right_on='id'))



data3 = {'id':[1,2,3,4,5],'gens':['m','f','m','m','f'],'age':[15,18,32,21,65],'job':['dv','dv','dv','NHJ','wdv'],'mariz':[True,False,False,False,True]}
df3=pd.DataFrame(data3)
print(df3)



print(pd.merge(df,df3,left_on='id',right_on='id'))



print(pd.merge(df,df3,how='left',left_on='id',right_on='id'))



print(pd.merge(df,df3,how='outer',left_on='id',right_on='id'))



data4 = {'id':[1,2,3,4,5],'gens':['m','f','m','m','f'],'age':[15,18,32,21,65],'job':['dv','dv','dv','NHJ','wdv'],'mariz':[False,False,False,False,True]}
df4=pd.DataFrame(data4)
print(df4)




print(pd.merge(df3,df4,left_on='id',right_on='id',suffixes=('_left','_right')))