import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9])

y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3


plt.title('Lines')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y1, linewidth=1,linestyle="-")
plt.plot(x, y2, linewidth=2,linestyle="--")
plt.plot(x, y3, linewidth=3,linestyle=":")
plt.show()