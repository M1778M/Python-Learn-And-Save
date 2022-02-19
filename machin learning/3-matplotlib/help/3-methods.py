import matplotlib.pyplot as plt
import numpy as np

Ys=[1,2,3,4,5]
pop = [122354,238223,31111,413232.24,383135]

plt.figure(figsize=(7,7),dpi=90) # figsize(5*4)
plt.plot(Ys,pop) # (x,y)

sc = np.array(pop)/10000
colors = ['red','green','orange','tomato','blue']

plt.title('MamadGang')
plt.xlabel('names')
plt.ylabel('pop')
plt.margins(0.1)
plt.xticks(Ys,['mamad','reza','fati','gholam','mamad2'])
plt.scatter(np.arange(5),pop,s=sc,c=colors)
plt.yticks([100000,200000,300000,700000],['1m','2m','3m','7m'])
plt.text(0,122354,'Mamad Jakon',fontsize=15)
plt.show()
