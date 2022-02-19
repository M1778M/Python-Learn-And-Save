import matplotlib.pyplot as plt
import numpy as np

#Styles
#plt.style.use('grayscale')

#plt.style.use('ggplot')

#plt.style.use('fivethirtyeight')

plt.style.use('dark_background')

#-----------------------

x = np.linspace(-10,10,100)

y = x ** 2

y2 = x ** -2

plt.plot(x,y,color='#fff',linewidth=4,linestyle='--')

plt.plot(x,y2,color='green',linewidth=2)


#--------------
plt.title('This Is Title')

plt.xlabel('X->IsN')

plt.ylabel('Y->IsN')
#-----------------

#all styles
print(plt.style.available)

#funny medar
#plt.xkcd()

# for append style (| , -) in medar use plt.grid()
plt.grid()

plt.legend(['x**2','x**-2'])

plt.show()
