import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 10000,10000)
# for y in range(1, 51):
#     z = x / (x + 300 + 50 * y)
#     plt.plot(x,  z, label = y)
# plt.legend()
# plt.show()
y = x / (x + 1000)
plt.plot(x,  y)
#z = np.power(x,0.3) / 100
#plt.plot(x,  z)
#plt.legend()
plt.show()