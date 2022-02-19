import matplotlib.pyplot as plt
import seaborn as sb
from pandas import read_csv

this = read_csv('D:\\Downloads\\test.csv')


#sb.boxplot(x='John',y='Riverside',data=this)


# sb.jointplot(x='John',y='Doe',data=this,kind='scatter')

# plt.show()


sb.pairplot(this,hue='John',palette='hls',plot_kws={'s':80})

plt.show()