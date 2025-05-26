import numpy as np

score = np.array([
    [99, 93, 60],
    [98, 82, 93],
    [93, 65, 81],
    [78, 82, 81]
])

result1 = score.sum()
print(result1)

result2 = score.min()
print(result2)

result3 = score.max()
print(result3)