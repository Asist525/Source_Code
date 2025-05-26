import numpy as np
import matplotlib.pyplot as plt

np.random.randn(10000)

Y1 = m, sigma = 10, 2
Y2 = m + sigma * np.random.randn(10000)

plt.figure(figsize=(10, 6))
plt.hist(Y1, bins=20)
plt.hist(Y2, bins=20)
plt.savefig("normal.png")