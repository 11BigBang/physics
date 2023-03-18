"""
Johns Hopkins University - MS Applied Physics
Electromagnetics
Midterm, Problem 4
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as spl

plt.style.use('bmh')

start = 0
end = np.pi
intervals = 10000

# Note that the theta values start just above 1 to avoid dividing by zero
eta = 376.73
thetas = np.linspace(0.00001, np.pi, intervals)
dtheta = (end - start)/intervals
ns = np.arange(1,11)

s_list = []
for n in ns:
    s = 0
    for theta in thetas:
        temp = (eta * np.pi/8) * (spl.jv(1, 2 * n * np.sin(theta)))**2 / np.sin(theta) *((np.cos(theta))**2 + 1) * dtheta
        s = s+temp
    s_list.append(s)

# Show graphically
fig, ax = plt.subplots()
ax.scatter(ns, s_list)
plt.xlabel('n')
plt.ylabel('Power (W)')
plt.show()