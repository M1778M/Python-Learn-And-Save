import pandas as pd


data = {'name':['mamad','reza','ali'],'gender':['m','m','m']}
df=pd.DataFrame(data)
print(df)



print(df.index)



print(list(df.index))


data2={'name':['fati','milad','zahra'],'gender':['f','m','f']}
df2 = pd.DataFrame(data2)
print(df2)


df_plus=df.append(df2,ignore_index=True)
print(df_plus)


df_plus.index+=1
print(df_plus)


df_plus.index = df_plus['name']


print(df_plus)


df_plus=df_plus.set_index('name')
print(df_plus)


df_plus=df_plus.reset_index()
print(df_plus)


