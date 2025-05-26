import numpy as np
import matplotlib.pyplot as plt

result1 = np.linspace(1, 10, 10000)
result2 = np.linspace(1, 20, 10000)
sin1 = np.sin(result1)
sin2 = np.sin(result2)

plt.plot(sin1)
plt.plot(sin2)
plt.savefig("sin.png")