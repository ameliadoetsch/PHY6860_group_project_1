import random
import matplotlib.pyplot as plt
import math

random1000 = [] # list for distribution of random numbers
i = 0
for i in range(1000): # 1000 random num
    random1000.append(random.random()) # gives each of 1000 numbers a random [0,1)

plt.figure(1) # label figure 1
plt.hist(random1000,10)  # plot with 10 bins
plt.title('Probability Distribution (10 bins)') # plot title
plt.show()
#print(random1000)

plt.figure(2) # label figure 2
plt.hist(random1000,20) # plot with 20 bins
plt.title('Probability Distribution (20 bins)') # plot title
plt.show()
#print(random1000)

plt.figure(3) # label figure 3
plt.hist(random1000,50) # plot with 50 bins
plt.title('Probability Distribution (50 bins)') # plot title
plt.show()
#print(random1000)

plt.figure(4) # label figure 4
plt.hist(random1000,100) # plot with 100 bins
plt.title('Probability Distribution (100 bins)') # plot title
plt.show()
#print(random1000)
#######################

random1000000 = [] # list for distribution of random numbers
i = 0
for i in range(1000000):  # 1000000 random num
    random1000000.append(random.random())  # gives each of 1000 numbers a random [0,1)

plt.figure(5)  # label figure 5
plt.hist(random1000000,10) # plot with 10 bins
plt.title('Probability Distribution (10 bins)') # plot title
plt.show()
#print(random1000000)

plt.figure(6) # label figure 6
plt.hist(random1000000,20) # plot with 20 bins
plt.title('Probability Distribution (20 bins)') # plot title
plt.show()
#print(random1000000)

plt.figure(7) # label figure 7
plt.hist(random1000000,50) # plot with 50 bins
plt.title('Probability Distribution (50 bins)') # plot title
plt.show()
#print(random1000000)

plt.figure(8) # label figure 8
plt.hist(random1000000,100) # plot with 100 bins
plt.title('Probability Distribution (100 bins)') # plot title
plt.show()
#print(random1000000)

#############################################################################################

# Part b

x_list = []
y_list = []
x_final = 1000
x_initial = 0
c = 1/(2 * math.pi)**(1/2)
x_sample = (x_final * random.random())
for x in range(x_final):
    x_sample = (x_final * random.random())
    x_list.append(x_sample)

for y in range(x_final):
    y_sample = (random.random())
    if y_sample <= c * math.exp((-1/2)*(x_sample**2)):
        y_list.append(y_sample)
    else:
         y_list.append(0)


plt.figure(9)
plt.title('Rejection Method')
plt.plot(x_list,y_list)
plt.show()

