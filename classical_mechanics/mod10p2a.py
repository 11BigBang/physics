"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Summer 2023, Classical Mechanics
Module 10, Problem 2, Part A
"""

import matplotlib.pyplot as plt
import numpy as np

# Set up time intervals and equation that yields beats
x = np.linspace(-5, 5, 1000)
V = np.abs(x)

plt.style.use('bmh')

# Plot
fig1, ax1 = plt.subplots()
ax1.plot(x, V)
ax1.plot(3, 3, 'ro')
ax1.plot(-3, 3, 'ro')
plt.xlabel("x")
plt.ylabel("V(\U000003BA=1)")
plt.show()