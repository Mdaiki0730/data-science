import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 7, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()
plt.savefig("E8.pdf", format='pdf', bbox_inches='tight')
