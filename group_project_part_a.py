import random
import matplotlib.pyplot as plt

# calculate array of 1000 random numbers from 0 to 1
rand = []
i = 0
while i < 1000:
    rand.append(random.random())
    i += 1

rand2 = []
i = 0
while i < 1000000:
    rand2.append(random.random())
    i += 1

# plot histogram of 1000 number array with 10, 20, 50, and 100 bins
plt.figure(1)
plt.hist(rand, 10)
plt.title("10 bins, 1000 values")
plt.show()

plt.figure(2)
plt.hist(rand, 20)
plt.title("20 bins, 1000 values")
plt.show()

plt.figure(3)
plt.hist(rand, 50)
plt.title("50 bins, 1000 values")
plt.show()

plt.figure(4)
plt.hist(rand, 100)
plt.title("100 bins, 1000 values")
plt.show()

# plot histogram of 1000000 number array with 10, 20, 50, and 100 bins
plt.figure(5)
plt.hist(rand2, 10)
plt.title("10 bins, 1000000 values")
plt.show()

plt.figure(6)
plt.hist(rand2, 20)
plt.title("20 bins, 1000000 values")
plt.show()

plt.figure(7)
plt.hist(rand2, 50)
plt.title("50 bins, 1000000 values")
plt.show()

plt.figure(8)
plt.hist(rand2, 100)
plt.title("100 bins, 1000000 values")
plt.show()
