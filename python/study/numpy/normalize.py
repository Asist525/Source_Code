import numpy as np
import matplotlib.pyplot as plt

m, sigma = 0, 0.1
result1 = np.random.normal(m, sigma, 500)
result2 = np.random.normal(0, 0.2, 500)
result3 = np.random.normal(0, 0.3, 500)
plt.plot(result1)
plt.plot(result2)
plt.plot(result3)

plt.savefig("normalize.png")
