import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb

this = pd.read_csv('D:\\Downloads\\example.csv')

print(this)

plt.scatter(this.inch,this.Weight,s=80)

plt.margins(0.05)
plt.xlabel('screen size')

plt.ylabel('weight')

plt.show()

print(np.mean(this.inch))
print(np.mean(this.Weight))

