import  matplotlib.pyplot as plt

years = [1960,1970,1980,1990,2000,2010,2020]
iranpop = [21.19,28.51,38.67,56.23,66.13,74.75,80.29]
tkpop = [27.47,34.88,43.98,53.92,63.24,72.33,79.51]

plt.subplot(1,2,1)
plt.plot(years,iranpop)
plt.title('iran')

plt.subplot(1,2,2)
plt.plot(years,tkpop)
plt.title('turkey')

plt.show()