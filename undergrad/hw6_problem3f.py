# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:54:21 2019

@author: Bryant Martin
"""

import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from scipy import signal
import os, time

x0 = 1.0
m = 0.1
b = 0.09
k = 0.1
w1 = np.sqrt((k/m)-(b*b))

def W(t):
    return (m*x0*x0*(k/m)*(k/m)/(2.0*w1*w1))*np.exp(-2.0*b*t)*(2.0*b*b*np.sin(w1*t)+b*w1*np.sin(2.0*w1*t)+(1.0-np.exp(2.0*b*t))*w1*w1)

# set time range
num=5000
time_range = 15.0   # total range time
dt = time_range/num # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array

plt.close('all') 

plt.figure(1)
plt.plot(t,W(t),'b', label="W(t)")
plt.xlabel('Time')
plt.ylabel('Work Done')
plt.title('Work Done on System')
plt.grid(True)