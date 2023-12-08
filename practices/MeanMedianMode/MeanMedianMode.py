import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create fake income data
# centered around: 27000
# standard deviation: 15000
# data points: 10000

incomes = np.random.normal(27000, 15000, 10000)

# Uncomment the following lines to see the histogram
# plt.hist(incomes, 50)
# plt.show()

print('===============================')

mean = np.mean(incomes)
print(f'The mean is: {mean}')

median = np.median(incomes)
print(f'The median is: {median}')

print('===============================')

# Now let's add Jeff Bezos into the mix
incomes = np.append(incomes, [1000000000])

mean = np.mean(incomes)
print(f'The mean after add Jeff Bezos is: {mean}')

median = np.median(incomes)
print(f'The median after add Jeff Bezos is: {median}')

print('===============================')

# Next, let's generate some fake age data for 500 people
# Minimum age: 18
# Maximum age: 90
# Data points: 500

ages = np.random.randint(18, high=90, size=500)
mode = stats.mode(ages)
print(f'The mode is: {mode}')

print('===============================')
