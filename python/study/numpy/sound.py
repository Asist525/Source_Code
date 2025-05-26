import numpy as np
import matplotlib.pyplot as plt

pure = np.linspace(1, 10, 100) # 1부터 10까지 100개의 난수 생성
noise = np.random.normal(0, 1, 100) # 평균이 0이고 표준편차가 1인 100개의 난수 생성
signal = pure + noise
plt.plot(signal)
plt.savefig("siganl.png")