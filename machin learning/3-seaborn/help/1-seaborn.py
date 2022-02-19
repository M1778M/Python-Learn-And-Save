import matplotlib.pyplot as plt
import seaborn as sb
from pandas import read_csv


this = read_csv('D:\\Downloads\\test.csv')

print(this)

sb.stripplot(x='John',y='Doe',data=this,size=10)

plt.show()


sb.swarmplot(x='John',y='Doe',data=this,size=10,hue='Riverside')

plt.show()