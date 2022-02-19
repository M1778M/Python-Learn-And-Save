import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

csvdf = pd.read_csv('data/datas.csv')

print(csvdf)

student = csvdf['student']

living_costs = csvdf['living_costs']

print(student)
print(living_costs)


#-------------------------

plt.style.use('dark_background')

plt.bar(student,living_costs)

plt.show()



#----------------------------- Big DataSet
this = 'ResponseId,MainBranch,Employment,Country,US_State,UK_Country,EdLevel,Age1stCode,LearnCode,YearsCode,YearsCodePro,DevType,OrgSize,Currency,CompTotal,CompFreq,LanguageHaveWorkedWith,LanguageWantToWorkWith,DatabaseHaveWorkedWith,DatabaseWantToWorkWith,PlatformHaveWorkedWith,PlatformWantToWorkWith,WebframeHaveWorkedWith,WebframeWantToWorkWith,MiscTechHaveWorkedWith,MiscTechWantToWorkWith,ToolsTechHaveWorkedWith,ToolsTechWantToWorkWith,NEWCollabToolsHaveWorkedWith,NEWCollabToolsWantToWorkWith,OpSys,NEWStuck,NEWSOSites,SOVisitFreq,SOAccount,SOPartFreq,SOComm,NEWOtherComms,Age,Gender,Trans,Sexuality,Ethnicity,Accessibility,MentalHealth,SurveyLength,SurveyEase,ConvertedCompYearly'.split(',')

dataset = pd.read_csv('data/dt.csv')

print(dataset.shape)

dataset_contry = dataset['Country']

orders = dataset_contry.value_counts()

print(orders)

orders = orders.to_dict()

cl = list(orders.keys())
amout = list(orders.values())

plt.bar(cl,amout)

plt.show()