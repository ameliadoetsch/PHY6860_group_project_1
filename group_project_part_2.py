import random
import matplotlib.pyplot as plt
import numpy as np

n = 100  # total time
m = 10000  # number of walkers

x_avg = np.arange(0, n, 1)
x2_avg = np.arange(0, n, 1)
n_arr = np.arange(0, n, 1)

i = 0

# 1D random walk (I assume this can be expanded into 2D??)
for j in range(m):
    x = 0
    for i in range(n):
        rand = random.random()
        if rand <= 0.5:
            x += -1
        else:
            x += 1
        # at each time step, we average over all the walkers (divide by m at this step to make code more concise)
        x_avg[i] += x / m
        x2_avg[i] += x ** 2 / m

# create plot average x v. time, average x2 v. time
plt.plot(n_arr, x_avg, label="avg x")
plt.plot(n_arr, x2_avg, label="avg x2")
plt.legend()
plt.show()
