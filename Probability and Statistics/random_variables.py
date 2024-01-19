import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# iris = sns.load_dataset('iris')
# print(iris.head())
# print(iris.species.unique())


# Titanic = sns.load_dataset('titanic')
# print(Titanic.head)
# print(Titanic.survived.unique())

"""
x = np.linspace(-20,20,10000)
mu = 1
sigma = 1
fx = np.exp((-(x-mu)**2) / (2*(sigma**2))) / ((2*np.pi*sigma**2) **0.5)

# print(fx)

plt.plot(x,fx)
plt.show() """

"""
x = np.linspace(-20,20,10000)
muz = np.arange(1,20,2)
for mu in muz:
    sigma = 1
    fx = np.exp((-(x-mu)**2) / (2*(sigma**2))) / ((2*np.pi*sigma**2) **0.5)
    plt.plot(x,fx)
# print(fx)
plt.show()
"""

"""
x = np.linspace(-20,20,10000)
mu = 0
sigmas = np.arange(1,10,2)
for sigma in sigmas:
    # sigma = 1
    fx = np.exp((-(x-mu)**2) / (2*(sigma**2))) / ((2*np.pi*sigma**2) **0.5)
    plt.plot(x,fx, label=str(sigma))
# print(fx)
plt.legend()
plt.show()
"""

# histogram

# W = np.random.exponential(scale=1, size=1000)
# X = np.random.normal(0,1,1000)
# Y = np.random.normal(10,10,1000)
# Z = np.random.normal(-10,4,1000)

# plt.hist(W, density=True, alpha = 0.5, bins = 30)
# plt.hist(X, density=True, alpha = 0.5, bins = 30)
# plt.hist(Y, density=True, alpha = 0.5, bins = 30)
# plt.hist(Z, density=True, alpha = 0.5, bins = 30)

# plt.show()

import seaborn as sb
# from icecream import ic

iris = sb.load_dataset('iris')
# # ic(iris)

# x = iris.sepal_length
# ic(plt.hist(x, density=True, bins=30))    
# plt.show()

# import random

# x = list()
# y = list()

# for i in range(0,100,10):
#     x.append(i)
#     # y.append(random.choice([1,100]))
#     y.append(random.randint(1,100))
    
# print(f"x: {x}\ny: {y}")

# plt.plot(x,y)
    
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Sample data
# data = np.random.normal(0, 1, 1000)

# # Non-normalized histogram
# plt.subplot(1, 2, 1)
# plt.hist(data, bins=30)
# plt.title('Non-Normalized Histogram')

# # Normalized histogram
# plt.subplot(1, 2, 2)
# plt.hist(data, density=True, bins=30)
# plt.title('Normalized Histogram')

sb.pairplot(iris, hue='species')
plt.show()








