import random
import matplotlib.pyplot as plt

random1000 = [] # list for distribution of random numbers
i = 0
for i in range(1000): # 1000 random num
    random1000.append(random.random()) # gives each of 1000 numbers a random [0,1)

plt.figure(1) # label figure 1
plt.hist(random1000,10)  # plot with 10 bins
plt.title('Probabiltiy Distribution (10 bins)') # plot title
plt.show()
print(random1000)

plt.figure(2) # label figure 2
plt.hist(random1000,20) # plot with 20 bins
plt.title('Probabiltiy Distribution (20 bins)') # plot title
plt.show()
print(random1000)

plt.figure(3) # label figure 3
plt.hist(random1000,50) # plot with 50 bins
plt.title('Probabiltiy Distribution (50 bins)') # plot title
plt.show()
print(random1000)

plt.figure(4) # label figure 4
plt.hist(random1000,100) # plot with 100 bins
plt.title('Probabiltiy Distribution (100 bins)') # plot title
plt.show()
print(random1000)
#######################

random1000000 = [] # list for distribution of random numbers
i = 0
for i in range(1000000):  # 1000000 random num
    random1000000.append(random.random())  # gives each of 1000 numbers a random [0,1)

plt.figure(5)  # label figure 5
plt.hist(random1000000,10) # plot with 10 bins
plt.title('Probabiltiy Distribution (10 bins)') # plot title
plt.show()
print(random1000000)

plt.figure(6) # label figure 6
plt.hist(random1000000,20) # plot with 20 bins
plt.title('Probabiltiy Distribution (20 bins)') # plot title
plt.show()
print(random1000000)

plt.figure(7) # label figure 7
plt.hist(random1000000,50) # plot with 50 bins
plt.title('Probabiltiy Distribution (50 bins)') # plot title
plt.show()
print(random1000000)

plt.figure(8) # label figure 8
plt.hist(random1000000,100) # plot with 100 bins
plt.title('Probabiltiy Distribution (100 bins)') # plot title
plt.show()
print(random1000000)

