import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from pandas import read_csv

this = read_csv('D:\\Downloads\\test.csv')

print(this)
print()

this_c = this.John.value_counts()
print(this_c,end='\n\n\n')
cat = this_c.index
print(cat)

plt.bar(cat,this_c)
plt.xlabel('index')
plt.ylabel('counts')

plt.xticks(([1,2,3,4]))
plt.yticks([1,2,3])
plt.show()

