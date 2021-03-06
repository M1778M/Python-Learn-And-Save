import sklearn
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

data = pd.read_csv('data/car.data',sep=',')

le = preprocessing.LabelEncoder()

buying = le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
doors = le.fit_transform(list(data['doors']))
persons = le.fit_transform(list(data['persons']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
cls = le.fit_transform(list(data['class']))

x = list(zip(buying,maint,persons,lug_boot,safety)) # features
y = list(cls) # labels

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

print(x_test)
