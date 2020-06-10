import matplotlib.pyplot as plt
import numpy as np
#import math

#抛物线
x = np.arange(-10, 10, 0.01)
y = x ** 2
plt.plot(x,y)
plt.show()

#log
x = np.arange(-10, 10, 0.01)
y = np.log(x)
plt.plot(x,y)
plt.show()

#幂函数
x = np.arange(-1, 1, 0.01)
y = 2 ** x
plt.plot(x,y)
plt.show()

x = np.arange(-10, 10, 0.01)
y = 2 ** x
plt.plot(x,y)
plt.show()
#plt.savefig()