"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Spring 2023, Electromagnetics
Homework 8, Problem 4
"""

import matplotlib.pyplot as plt
import numpy as np

N = 1000
start = 1
end = 5

# Declare natural constants and those given in problem statement
mu_0 = 4 * np.pi * 10**(-7)
eps_0 = 8.854 * 10**(-12)
omega_p = 2 * np.pi * 10**6
nu = 2 * np.pi * 10**3

# Generates a 'continuum' of frequencies on a MHz scale then converts to angular frequecies
Mfreqs = np.linspace(start, end, N)
ang_freqs = Mfreqs * 2 * np.pi * 10**6
delta_f = (end - start)/N * np.pi * 10**6


eps_r = 1 - (omega_p**2)/(nu**2 + ang_freqs**2)
eps_i = (omega_p**2*nu)/(ang_freqs*nu**2 + ang_freqs**3)
k_0 = ang_freqs * np.sqrt(mu_0 * eps_0)

# Generates lists for beta_i and phase and group velocities based on angular frequencies
beta_i = -k_0/np.sqrt(2) * (-eps_r + np.sqrt(eps_r**2 + eps_i**2))**(0.5)
beta_r = -(k_0**2 * eps_i)/(2 * beta_i)
phase_velo = ang_freqs/beta_r


# i, group_velo = 0, []
# while i <= len(beta_r):
#     group_velo.append((beta_r[i+1] - beta_r[i])/delta_f)
#     i =+ 1
    
# group_velo.append(group_velo[-1]) # Tacks another value onto end just to give same number of datapoint


plt.style.use('bmh')

#Show graphically
fig1, ax1 = plt.subplots()
ax1.plot(Mfreqs, eps_r)
plt.xlabel('Frequency (MHz)')
plt.ylabel('Permittivity (real)')
plt.legend()
plt.show()

# Show graphically
fig2, ax2 = plt.subplots()
ax2.plot(Mfreqs, phase_velo)
# ax2.plot(Mfreqs, group_velo)
plt.xlabel('Frequency (MHz)')
ax2.set_yscale('log')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.show()