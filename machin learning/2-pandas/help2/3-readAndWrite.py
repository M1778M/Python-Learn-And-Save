import pandas as pd


countries = pd.read_csv('csv/countries.csv',header=0,sep=",",names=['id','code','name','continent','link','keywords'],encoding='utf-8')


countries.to_csv('country1.csv',index=False) # Save File