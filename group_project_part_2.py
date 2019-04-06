import random
import matplotlib.pyplot as plt
import numpy as np

n = 100  # total time
m = 10000  # number of walkers

x_avg = np.zeros(n)
x2_avg = np.zeros(n)
n_arr = np.arange(0, n, 1)
xlist = np.zeros(n)
ylist = np.zeros(n)
MSDList = np.zeros(50)
deca = np.arange(0, 50, 1)
i = 0

for l in deca:    # 2D random walk
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


            ## tracking x and y values for diffusion
            xlist[i] = x
            ylist[i] = y

    ## Declare List for the radius and square difference between each position
    rlist = []
    diffsq = []
    for i in n_arr:
        # calculate radius
        rlist.append(np.sqrt(xlist[i]**2 + ylist[i]**2))
        # calculate the diff between steps, square it and multiply by the probability (0.25)
        diffsq.append(0.25 * (rlist[i]-rlist[i-1])**2)

    ## find the mean of the square diff
    MSD = np.mean(diffsq)
    MSDList[l] = MSD

## Return mean square difference
print(np.mean(MSDList))


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


