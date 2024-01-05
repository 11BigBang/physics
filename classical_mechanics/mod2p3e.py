"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Summer 2023, Classical Mechanics
Module 2, Problem 3, Part E
"""

import matplotlib.pyplot as plt
import numpy as np

E_0 = 1
B_0 = 1
omega_c = 1

# ISSUE WITH UNITS - this is in rad/s where it should be Hz
t = np.linspace(0, 25, 1000)
x = (E_0/B_0)*(t - (1/omega_c)*np.sin(omega_c * t))
y = (E_0/(B_0 * omega_c))*(1 - np.cos(omega_c * t))

plt.style.use('bmh')

# Plot
fig1, ax1 = plt.subplots()
ax1.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()