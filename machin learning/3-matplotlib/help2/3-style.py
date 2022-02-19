import matplotlib.pyplot as plt
import numpy as np

#Styles
#plt.style.use('grayscale')

plt.style.use('ggplot')

#plt.style.use('fivethirtyeight')


#-----------------------
# figure setting
plt.figure(figsize=(10,5),dpi=100)
#---------

x = np.linspace(-5,5,10)

y = x ** 2

y2 = x ** -2

plt.plot(x,y,color='#000',linewidth=2,linestyle='-.',marker='*',markersize=10,label='IsKhat')


#--------------
plt.title('This Is Title')

plt.xlabel('X->IsN')

plt.ylabel('Y->IsN')
#-----------------

#all styles
print(plt.style.available)

#funny medar
plt.xkcd()

# for append style (| , -) in medar use plt.grid()
#plt.grid()

plt.legend()


plt.savefig('.\\matplotlib.png') # pdf , wav , jpg , ...

plt.show()
