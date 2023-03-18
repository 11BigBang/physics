"""
Johns Hopkins University - MS Applied Physics
Electromagnetics
Self Check 4, Problem 3
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

f = 50

#Create list of t0 values that will yield only real images and find t0-t1
theta = np.linspace(0, np.pi, 1000)
E = 7336.1 * np.sin(theta)

#Show graphically
fig, ax = plt.subplots()
ax.plot(theta, E)
plt.xlabel('\U000003B8')
plt.ylabel('E')
plt.legend()
plt.show()