"""
William "Bryant" Martin
Johns Hopkins University - MS Applied Physics
Spring 2023, Electromagnetics
Self Check 10, Problem 1-5
"""

import matplotlib.pyplot as plt
import numpy as np

# Sets the characteristics of the 2 media - no other modifications necessary
mu_1r = 1
eps_1r = 1
mu_2r = 1
eps_2r = 81

# Sets angle for independent variable, converts to radians for math, and finds transmitted angle using Snell's Law
theta_i_deg = np.linspace(0, 90, 1000)
theta_i = np.deg2rad(theta_i_deg)
theta_t = np.arcsin(np.sqrt(mu_1r * eps_1r) * np.sin(theta_i)/np.sqrt(mu_2r * eps_2r))

# Natural constants
mu_0 = 4 * np.pi * 10**(-7)
eps_0 = 8.854 * 10**(-12)

# Calculates values of wave impedance for both media
eta_1 = np.sqrt((mu_0 * mu_1r)/(eps_0 * eps_1r))
eta_2 = np.sqrt((mu_0 * mu_2r)/(eps_0 * eps_2r))

def brewster_coeff(Rs):
    low = 10
    has_negative, has_positive, has_brewster = False, False, False
    for R in Rs:
        if abs(R) < abs(low):
            low = R

    if abs(low) > 0.01:
        return 10
    return low

# TM wave coefficients
R_par = (eta_2 * np.cos(theta_t) - eta_1 * np.cos(theta_i))/(eta_2 * np.cos(theta_t) + eta_1 * np.cos(theta_i))
T_par = (2 * eta_2 * np.cos(theta_i))/(eta_2 * np.cos(theta_t) + eta_1 * np.cos(theta_i))
# Find the Brewster angle (R=0), if it exists
TM_bc = brewster_coeff(R_par)
if TM_bc == 10:
    TM_brewster_index = 0
    TM_brewster = 0
    TM_brewster_label = 'No Brewster Angle Exists'
else:
    TM_brewster_index = np.where(R_par == brewster_coeff(R_par))
    TM_brewster = theta_i_deg[TM_brewster_index]
    TM_brewster_label = f'Brewster Angle ({round(TM_brewster[0])} degrees)'

# TE wave coefficients
R_perp = (eta_2 * np.cos(theta_i) - eta_1 * np.cos(theta_t))/(eta_2 * np.cos(theta_i) + eta_1 * np.cos(theta_t))
T_perp = (2 * eta_2 * np.cos(theta_i))/(eta_2 * np.cos(theta_i) + eta_1 * np.cos(theta_t))
# Find the Brewster angle (R=0), if it exists
TE_bc = brewster_coeff(R_perp)
if TE_bc == 10:
    TE_brewster_index = 0
    TE_brewster = 0
    TE_brewster_label = 'No Brewster Angle Exists'
else:
    TE_brewster_index = np.where(R_perp == brewster_coeff(R_perp))
    TE_brewster = theta_i_deg[TE_brewster_index]
    TE_brewster_label = f'Brewster Angle ({round(TE_brewster[0])} degrees)'

plt.style.use('bmh')

# Plot coefficients for TM wave
fig1, ax1 = plt.subplots()
ax1.plot(theta_i_deg, R_par, label="R Parallel")
ax1.plot(theta_i_deg, T_par, label="T Parallel")
if TM_bc != 10:
    ax1.scatter(TM_brewster, R_par[TM_brewster_index], label=TM_brewster_label, color='g')
else:
    ax1.text(0, 0, 'No Brewster Angle Exists', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.xlabel("Incident Angle (degrees)")
plt.ylabel("Reflection and Transmission Coefficient")
plt.legend()
plt.show()

# Plot coefficients for TE wave
fig2, ax2 = plt.subplots()
ax2.plot(theta_i_deg, R_perp, label="R Perpendicular")
ax2.plot(theta_i_deg, T_perp, label="T Perpendicular")
if TE_bc != 10:
    ax2.scatter(TE_brewster, R_perp[TE_brewster_index], label=TE_brewster_label, color='g')
else:
    ax2.text(0, 0, 'No Brewster Angle Exists', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.xlabel("Incident Angle (degrees)")
plt.ylabel("Reflection and Transmission Coefficient")
plt.legend()
plt.show()