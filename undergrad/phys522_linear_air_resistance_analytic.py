# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:19:38 2015
Revised January 2019

Linear air resistance on a oil drop
Based on book example 2.2

launch an oil drop straigt up with speed vy0 from y=0.  
Plot v(t) and y(t)


@author: Brian Washburn
"""
import numpy as np
from matplotlib import pyplot as plt
import os

# physical parameters, all in mks units
g = 9.81                    # gravitational acceleration near the earth
d = 0.2e-3                 # drop diameter
beta = 1.6e-4               # coefficient of linear air resistance
density = 997             # oil density
m = density*np.pi*(4/3)*((d/2)**3)    # ball mass
b = beta*d                  # linear force coefficient 
vterm = m*g/b               # terminal speed
tau = vterm/g               # time constant
k = b/m                     # define constant k

print ('-----------------------------------------------------------------------')
print ('Running %s ...' % os.path.basename(__file__),)
print (' ' )
print (' ')
print ('Terminal speed is %0.3g m/s' % vterm)
print ('Time constant tau is %0.3g s' % tau)

# Determine the time of flight by plotting
num=5000
time_range = 5*tau   # total range time
dt = time_range/num # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array

vx0 = 0.0
vy0 = -5 # -5.0e-5

vy = vy0*np.exp(-t/tau) + vterm*(1 - np.exp(-t/tau))
y = vterm*t + (vy0 - vterm)*tau*(1 - np.exp(-t/tau))

plt.figure(1)
plt.plot(t/1e-6, vy,'r', label = r'$v(t)$')
plt.plot(t/1e-6,vterm*np.ones(num),'g',label= r'$v_{term}$')
plt.xlabel(r'$t\ (\mu s)$')
plt.ylabel(r'$v_{y}\ (m/s)$')
plt.title(r'$v_{y}$ vs $t$')
plt.grid(True)
plt.legend(loc=4)

plt.figure(2)
plt.plot(t/1e-6, y)
plt.xlabel(r'$t\ (\mu s)$')
plt.ylabel('y(t)')
plt.title('height vs time')
plt.grid(True)
