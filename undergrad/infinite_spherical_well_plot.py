# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:02:45 2020

@author: wbmar
"""
#instructions:  just change l to get the plots and values for zeros of bessel

from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
import sys

l = 2

xvals = np.linspace(0, 20,10000)
n, hbar, a, m = sp.symbols('hbar a m n') 

if l == 0:
    sp.pprint('The energy level for these is simply ',(n**2*np.pi**2*hbar**2)/(2*m*a**2))
    sys.exit()
elif l == 1:
    y1 = np.cos(xvals)/xvals
    y2 = np.sin(xvals)/xvals**2
    energyx = [4.493,7.725,10.904]
    def l1func(q):
        energyy = np.cos(q)/q
        return energyy
elif l == 2:
    y1 = (3/xvals**3-1/xvals)*np.sin(xvals)
    y2 = 3/(xvals**2)*np.cos(xvals)
    energyx = [5.763,9.095,12.323]
    def l1func(q):
        energyy = 3/(q**2)*np.cos(q)
        return energyy
elif l == 3:
    y1 = (15/xvals**2-1)*np.cos(xvals)/xvals
    y2 = (15/xvals**3-6/xvals)*np.sin(xvals)/xvals
    energyx = [6.988,10.417,13.698]
    def l1func(q):
        energyy = (15/q**2-1)*np.cos(q)/q
        return energyy
elif l == 4:
    
    y1 = -1*(xvals**4*np.sin(xvals))/xvals**5
    y2 = (10*xvals**3*np.cos(xvals) - 45*xvals**2*np.sin(xvals) - 105*xvals*np.cos(xvals) + 105*np.sin(xvals))/xvals**5
    energyx = [8.183,11.705,15.040]
    def l1func(q):
        energyy = -1*(q**4*np.sin(q))/q**5
        return energyy
else:
    "can only calculate l up to 4"

# plotting the points
plt.figure(1) 
plt.plot(xvals, y1, label= 'left side')
plt.plot(xvals, y2, label= 'right side')
for i in range(0,3):
    plt.plot(energyx[i],l1func(energyx[i]), 'ro')
    plt.text(energyx[i],l1func(energyx[i]),energyx[i])

# plt.yticks(np.linspace(0, 10,1))
#plt.plot(xvals, y, label='Potential') 
plt.xlabel('x')
plt.xlim(0,20)
plt.ylim(-0.5,1)
plt.ylabel('Functions')
plt.title('Infinite Spherical Well')
plt.legend()

