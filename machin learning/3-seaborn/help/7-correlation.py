import matplotlib.pyplot as plt
import numpy as np

import seaborn as sb

rand = np.random.random(3)

print(rand)

rand2 = np.random.random(1000)

win = rand>0.5

w = rand2 > 0.5

numH = np.sum(w)/1000

print(numH)
print(win)

tmp = np.random.normal(0,1,1000)

print(tmp)

sb.displot(tmp)
plt.show()