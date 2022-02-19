import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from pandas import read_csv

this = read_csv('D:\\Downloads\\test.csv')


this_c = this.John.value_counts()

def ECDF(data):
    n=len(data)
    x=np.sort(data)
    y=np.arange(1,n+1)/n
    return x,y

x,y=ECDF(this.inch)
print(x,'\n',y)

plt.figure(figsize=(1,7))
plt.scatter(x,y,s=80)
plt.margins(0.85)
plt.xlabel('inch',fontsize=13)
plt.ylabel('ECDF',fontsize=13)
plt.show()