import random
import matplotlib.pyplot as plt
import numpy as np

n = 100  # total time
m = 10000  # number of walkers

x_avg = np.zeros(n)
x2_avg = np.zeros(n)
n_arr = np.arange(0, n, 1)

i = 0

# 2D random walk
for j in range(m):
    x = 0
    y = 0
    for i in range(n):
        rand = random.random()
        if rand <= 0.25:
            x += -1
        elif rand <= 0.5 and rand > 0.25:
            x += 1
        elif rand <= 0.75 and rand > 0.5:
            y += 1
        else:
            y += -1
        # at each time step, we average over all the walkers (divide by m at this step to make code more concise)
        x_avg[i] += x / m
        x2_avg[i] += x ** 2 / m

# create plot average x v. time, average x2 v. time
plt.figure(1)
plt.plot(n_arr, x_avg)
plt.title("10${^4}$ Random Walkers on 2D Lattice")
plt.xlabel("Time")
plt.ylabel("<x>")
plt.show()

plt.figure(2)
plt.plot(n_arr, x2_avg)
plt.title("10${^4}$ Random Walkers on 2D Lattice")
plt.xlabel("Time")
plt.ylabel("<x${^2}$>")
plt.show()

