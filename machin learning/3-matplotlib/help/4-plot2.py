import matplotlib.pyplot as plt

years = [1960,1970,1980,1990,2000,2010,2020]
iranpop = [21.19,28.51,38.67,56.23,66.13,74.75,80.29]
tkpop = [27.47,34.88,43.98,53.92,63.24,72.33,79.51]

plt.plot(years,iranpop,ls='-',marker='+',mew=8)
plt.plot(years,tkpop,ls='--',lw=1)
plt.title('iran vs turkey')
plt.legend(['iran','turkey'],loc='best')
plt.xlabel('years')
plt.ylabel('pops')
plt.yticks([20,30,40,50,60,70,80],['20m','30m','40m','50m','60m','70m','80m'])
plt.grid()
plt.annotate('Iran in 1990',xytext=(1990,40),xy=(1990,56.2),arrowprops={'facecolor' : 'blue','width' : 4},fontsize=10)
plt.show()