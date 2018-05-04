#!/usr/bin/python3

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array(range(1,9))
quadratic_data = linear_data**2

plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')

plt.show()
