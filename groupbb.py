import random
import matplotlib.pyplot as plt
import math

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
plt.hist(rand_thousand, 10)
plt.title("Uniform Probability Distribution, 1,000 samples in 10 bins")
plt.show()

plt.figure(2)
plt.hist(rand_thousand, 20)
plt.title("Uniform Probability Distribution, 1,000 samples in 20 bins")
plt.show()

plt.figure(3)
plt.hist(rand_thousand, 50)
plt.title("Uniform Probability Distribution, 1,000 samples in 50 bins")
plt.show()

plt.figure(4)
plt.hist(rand_thousand, 100)
plt.title("Uniform Probability Distribution, 1,000 samples in 100 bins")
plt.show()

# plot histogram of 1000000 number array with 10, 20, 50, and 100 bins
plt.figure(5)
plt.hist(rand_million, 10)
plt.title("Uniform Probability Distribution, 1,000,000 samples in 10 bins")
plt.show()

plt.figure(6)
plt.hist(rand_million, 20)
plt.title("Uniform Probability Distribution, 1,000,000 samples in 20 bins")
plt.show()

plt.figure(7)
plt.hist(rand_million, 50)
plt.title("Uniform Probability Distribution, 1,000,000 samples in 50 bins")
plt.show()

plt.figure(8)
plt.hist(rand_million, 100)
plt.title("Uniform Probability Distribution, 1,000,000 samples in 100 bins")
plt.show()

#############################################################################################

# Part b

x_list = [] # list for sampled x
x_initial = 0
c = 1/((2 * math.pi)**(1/2)) # constant for p
i = 0
n = 0

while n < 1000: # sample 1000 x points
    x_sample = (10*random.random() -5) # sample x point between -5 and 5 points
    y_sample = c * (random.random()) # sample y point between 0 and 1 points
    if y_sample <= c * math.exp((-1/2) * (x_sample**2)): # if y is less than p append to list
        n+=1
        x_list.append(x_sample)  # append each of these samples to list

plt.figure(9)
plt.title('Rejection Method 10 bins')
plt.hist(x_list, 10)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(10)
plt.title('Rejection Method 20 bins')
plt.hist(x_list, 20)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(11)
plt.title('Rejection Method 50 bins')
plt.hist(x_list, 50)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(12)
plt.title('Rejection Method 100 bins')
plt.hist(x_list, 100)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()
