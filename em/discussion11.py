"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Spring 2023, Electromagnetics
Self Check 10, Problem 1-5
"""

import matplotlib.pyplot as plt
import numpy as np


eps_0 = 8.854 * 10**(-12)
N_e = 10**12
q_e = -1.602 * 10**(-19)
B_0 = 45 * 10**(-6)
m_e = 9.109 * 10**(-31)

# ISSUE WITH UNITS - this is in rad/s where it should be Hz
omega_MHz = np.linspace(20, 50, 1000)
omega_Hz = omega_MHz * 1000000

omega_g = -q_e*B_0/m_e
omega_p = np.sqrt((N_e*q_e**2)/(eps_0*m_e))

eps_gr = (omega_g * omega_p**2)/(omega_Hz*(omega_Hz**2 - omega_g**2))
eps_r = 1 - omega_p**2/(omega_Hz**2 - omega_g**2)
eps_zr = 1 - omega_p**2/omega_Hz**2

plt.style.use('bmh')

# Plot coefficients for TM wave
fig1, ax1 = plt.subplots()
ax1.plot(omega_MHz, eps_gr, label="Gyroscopic")
# ax1.plot(omega_MHz, eps_r, label="Epsilon")
# ax1.plot(omega_MHz, eps_zr, label="Epsilon z")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Relative Permittivity")
plt.legend()
plt.show()
