import matplotlib.pyplot as plt


names = ['mamad','ali','reza','sara','gholam','sakine']
sens = [24,11,19,39,32,23]

plt.pie(sens,labels=names)
plt.show()


years=[1900,1901,1902,1903,1904]
pop = [1.3,2.5,3.1,4.24,5]

plt.figure(figsize=(7,7),dpi=100) # figsize(5*4)
plt.plot(years,pop) # (x,y)
plt.xlabel('years')
plt.ylabel('pop')
plt.yticks(pop,[str(i)+'-N' for i in pop])
plt.xticks(years,[str(i)+'Y' for i in years])
plt.show()