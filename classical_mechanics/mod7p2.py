"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Summer 2023, Classical Mechanics
Module 7, Problem 2
"""

import matplotlib.pyplot as plt
import numpy as np

omega_1, omega_2 = 1.0, 1.1

# Set up time intervals and equation that yields beats
t = np.linspace(0, 200, 1000)
y = 2*np.sin((omega_1+omega_2)*t)*np.sin((omega_1-omega_2)*t)

plt.style.use('bmh')

# Plot
fig1, ax1 = plt.subplots()
ax1.plot(t, y)
plt.xlabel("t")
plt.ylabel("y")
plt.show()