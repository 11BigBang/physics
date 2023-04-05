"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Spring 2023, Electromagnetics
Homework 8, Problem 3
"""

import matplotlib.pyplot as plt
import numpy as np

# Declare natural constants and those given in problem statement
mu_0 = 4 * np.pi * 10**(-7)
eps_0 = 8.854 * 10**(-12)
omega_p = 2 * np.pi * 10**9
omega_0 = 6 * np.pi * 10**9

# Generates a 'continuum' of frequencies on a GHz scale then converts to angular frequecies
Gfreqs = np.linspace(0, 5, 1000)
ang_freqs = Gfreqs * 2 * np.pi * 10**9

# Generates lists for phase and group velocities based on angular frequencies
phase_velos = (mu_0*eps_0*(1 + omega_p**2/(omega_0**2 - ang_freqs**2)))**(-0.5)
group_velos = 1/(np.sqrt(mu_0*eps_0)) * ((1 + omega_p**2/(omega_0**2-ang_freqs**2))**(0.5) \
              + ang_freqs**2 * omega_p**2 * (1 + omega_p**2/(omega_0**2-ang_freqs**2))**(-0.5) \
              * (omega_0**2-ang_freqs**2)**(-2))**(-1) 

#Show graphically
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(Gfreqs, phase_velos, label='phase velocity')
ax.plot(Gfreqs, group_velos, label='group velocity')
ax.set_yscale('log')
plt.xlabel('Frequency (GHz)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.show()