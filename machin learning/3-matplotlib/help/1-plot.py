#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

years=[1900,1901,1902,1903,1904]
pop = [1.3,2.5,3.1,4.24,5]

plt.plot(years,pop) # (x,y)

plt.show()

plt.scatter(years,pop)
plt.show()

sens = [24,11,19,39,32,23]

plt.hist(sens,bins='auto')
plt.show()