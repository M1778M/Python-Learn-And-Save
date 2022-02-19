import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5,6,7,8,9])

y = x ** 2


plt.plot(x,y)

plt.show()

#------------------------------------

x = np.linspace(-10,10,100)

y = x ** 2

y2 = x ** -2

plt.plot(x,y,color='#000')

plt.plot(x,y2,color='green')

plt.title('This Is Title')
plt.xlabel('X->IsN')
plt.ylabel('Y->IsN')

plt.legend(['x**2','x**-2'])

plt.show()

