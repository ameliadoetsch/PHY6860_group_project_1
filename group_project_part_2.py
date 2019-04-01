import random
import matplotlib.pyplot as plt
import numpy as np

n = 100  # total time
m = 10000  # number of walkers

def create_zero_arrays():
    i = 0
    array = []
    for i in range(n):
        array.append(0)
    return array


x_avg = create_zero_arrays()
x2_avg = create_zero_arrays()
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
        #does he want us to just find avg(x2) or like the average of the total displacement squared? since it's 2D
        #d = np.sqrt(x ** 2 + y ** 2)
        d = x
        x_avg[i] += d / m
        x2_avg[i] += d ** 2 / m

# create plot average x v. time, average x2 v. time
plt.plot(n_arr, x_avg, label="avg x")
plt.plot(n_arr, x2_avg, label="avg x2")
plt.legend()
plt.show()
