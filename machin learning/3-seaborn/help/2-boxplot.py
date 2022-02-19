import matplotlib.pyplot as plt
import seaborn as sb
from pandas import read_csv

this = read_csv('D:\\Downloads\\test.csv')


sb.boxplot(x='John',y='Riverside',data=this)

plt.show()