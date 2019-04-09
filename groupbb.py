import random
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
from scipy import stats

# Part b

x_list = [] # list for sampled x
y = []
x_initial = 0
c = 1/((2 * math.pi)**(1/2)) # constant for p
i = 0
n = 0

# Accept points if less than p and appends to list
while n < 1000: # sample 1000 x points
    x_sample = (10*random.random() - 5) # sample x point between -5 and 5 points
    y_sample = c * (random.random()) # sample y point between 0 and 1 points
    if y_sample <= c * math.exp((-1/2) * (x_sample**2)): # if y is less than p append to list
        n+=1
        x_list.append(x_sample) # append each of these samples to list

xx = np.arange(-5, +5, 0.001)
yy = stats.norm(0,1).pdf(xx)
# plot histogram gaussian distribution 1,000 number array 10, 20, 50, 100
plt.figure(9)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 10)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000 samples (10 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()


plt.figure(10)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 20)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000 samples (20 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(11)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 50)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000 samples (50 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(12)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 100)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000 samples (100 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

# Accept points if less than p and appends to list
while n < 1000000: # sample 1,000,000 x points
    x_sample = (10*random.random() -5) # sample x point between -5 and 5 points
    y_sample = c * (random.random()) # sample y point between 0 and 1 points
    if y_sample <= c * math.exp((-1/2) * (x_sample**2)): # if y is less than p append to list
        n+=1
        x_list.append(x_sample)  # append each of these samples to list
# plot histogram gaussian distribution 1,000,000 number array 10, 20, 50, 100
plt.figure(13)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 10)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000,000 samples (10 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(14)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 20)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000,000 samples (20 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(15)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 50)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000,000 samples (50 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

plt.figure(16)
ax = sns.distplot(x_list, kde = False, norm_hist=True, bins = 100)
ax.plot(xx, yy, 'r', lw=2) #Lw is line width, 'r' is red color
plt.title('Gaussian Distribution 1,000,000 samples (100 bins)')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

