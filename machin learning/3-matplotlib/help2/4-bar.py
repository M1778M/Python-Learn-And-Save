import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)

plt.style.use('seaborn')

#---------------------------
dev_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46752, 49320, 53200, 
    56000, 62316, 64928, 67317, 68748, 73752]
py_dev_x = dev_x
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49963, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
#-----------------------------

# bars
plt.bar(dev_x,py_dev_y,label='pythonDev',linewidth=2,alpha=0.6)

plt.bar(dev_x,js_dev_y,label='JavaScriptDev',linewidth=2,color='yellow',alpha=0.6)

plt.bar(dev_x,dev_y,label='Developers',linewidth=2,color='purple',alpha=0.6)
# plots
plt.plot(dev_x,py_dev_y,label='pythonDev',linewidth=2)

plt.plot(dev_x,js_dev_y,label='JavaScriptDev',linewidth=2,color='yellow')

plt.plot(dev_x,dev_y,label='Developers',linewidth=2,color='purple')


plt.legend()

plt.show()