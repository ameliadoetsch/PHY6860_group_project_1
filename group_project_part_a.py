import random
import matplotlib.pyplot as plt

# calculate array of 1000 random numbers from 0 to 1
rand_thousand = []
i = 0
for i in range(1000):
    rand_thousand.append(random.random())

rand_million = []
i = 0
for i in range(1000000):
    rand_million.append(random.random())

# plot histogram of 1000 number array with 10, 20, 50, and 100 bins
plt.figure(1)
plt.hist(rand_thousand, 10, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000 samples in 10 bins")
plt.show()

plt.figure(2)
plt.hist(rand_thousand, 20, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000 samples in 20 bins")
plt.show()

plt.figure(3)
plt.hist(rand_thousand, 50, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000 samples in 50 bins")
plt.show()

plt.figure(4)
plt.hist(rand_thousand, 100, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000 samples in 100 bins")
plt.show()

# plot histogram of 1000000 number array with 10, 20, 50, and 100 bins
plt.figure(5)
plt.hist(rand_million, 10, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000,000 samples in 10 bins")
plt.show()

plt.figure(6)
plt.hist(rand_million, 20, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000,000 samples in 20 bins")
plt.show()

plt.figure(7)
plt.hist(rand_million, 50, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000,000 samples in 50 bins")
plt.show()

plt.figure(8)
plt.hist(rand_million, 100, edgecolor='white')
plt.title("Uniform Probability Distribution, 1,000,000 samples in 100 bins")
plt.show()
