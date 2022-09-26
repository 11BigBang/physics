# -*- coding: utf-8 -*-
"""
Compute Fourier series of a symmetric square pulse of amplitude f0
period TD and width DT

f(t) = an*cos(n*wd*t) + bn*sin(n*wd*t)

@author: Brian Washburn
"""

import numpy as np
from matplotlib import pyplot as plt
import os, time

start=time.time()                   # start cpu time

# f(t) parameters
f0 = 1.0         # amplitude of driving force F/m
wd = 2*np.pi       # driving frequency (will vary), book value wd=w0/5
TD = 2*np.pi/wd     # drive period, book value 1 s
DT = 0.1

# set time range
num=10000
time_range = 4*TD   # total range time
dt = time_range/num # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array


print ('-----------------------------------------------------------------------')
print ('Running %s ...' % os.path.basename(__file__),)
print (' ' )
print ('The drive frequency is %0.2f rad/s' % wd)
print ('The drive period is %0.2f s' % TD)

# terms for the Fourier series
a0 = f0*DT/TD

def a(n):
    # here n = 1,2,3,...
    return (2*f0/(np.pi*n))*np.sin(np.pi*n*DT/TD)
    
def b(n):
    # here n = 1,2,3,...
    return 0.0

N = 100
an = []
bn = []

fs = a0
 
for ni in np.arange(N)+1 :
    an.append(a(ni))
    bn.append(b(ni))
    fs = fs + an[ni-1]*np.cos(ni*wd*t) + bn[ni-1]*np.sin(ni*wd*t)

plt.close('all') 

plt.figure(1)
plt.plot(t,fs)
plt.xlabel('time (s)')
plt.ylabel('f(t)')
plt.rc('lines', linewidth=0.5)
plt.grid(True)
#plt.xlim([0.9,1.1])

plt.figure(2)
plt.bar(np.arange(N),an,0.5)
plt.xlabel('n')
plt.ylabel('an')
plt.grid(True)

plt.figure(3)
plt.bar(np.arange(N),bn,0.5)
plt.xlabel('n')
plt.ylabel('bn')
plt.grid(True)

runtime=(time.time() - start)  # stop cpu time

print (' ' )
print ('Runtime of %0.2f seconds' % runtime)