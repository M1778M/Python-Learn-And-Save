import sklearn.model_selection
import numpy as np
import pandas as pd
from sklearn import linear_model
import pickle


data = pd.read_csv("data/student-mat.csv",sep=';')


data = data[['G1','G2','G3','studytime','failures','absences']]


predict = 'G3'

x = np.array(data.drop([predict],1))

y = np.array(data[predict])

# best=0

# for i in range(100):
#     x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

#     linear = linear_model.LinearRegression()
    
#     linear.fit(x_train,y_train)

#     acc = linear.score(x_test,y_test)

#     print(acc)

#     if (acc>best):
#         best=acc
#         with open('stdmodel.alg','wb') as f:
#             pickle.dump(linear,f)


# print("Best : ",best)

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

newModel = pickle.load(open('stdmodel.alg','rb'))

print("Coefficient:",newModel.coef_)

print("Intercept:",newModel.intercept_)

result = newModel.predict(x_test)

for x in range(len(result)):
    print(result[x],x_test[x],y_test[x])
