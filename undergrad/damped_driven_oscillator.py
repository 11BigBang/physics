# -*- coding: utf-8 -*-
"""
Solve the equation of motion for a damped,
drivien oscillator using Runge-Kutta

Based on example 5.3

The natural freuqncy is set to 5*(2*np.pi) for the book
example of a drive frequency of (2*np.pi).  Write the code
so we can vary the drive frequency by keep the natural
frequency and the damping the same.  Trancients will die out after 4 seconds.

Plot amplitude and phase as a function of drive frequency

@author: Brian Washburn
"""

import numpy as np
from scipy.integrate import ode
from matplotlib import pyplot as plt
from scipy import signal
import os, time

start=time.time()                   # start cpu time

# physical parameters, all in mks units
g = 9.81              # gravitational acceleration near the earth

# oscillator parameters
w0 = 1.0    # natural frequency, fixed at book value of w0 = (2*np.pi)
t0 = 2*np.pi/w0     # natural period
b = 0.1           # damping, choose to be underdamped
wr = np.sqrt(w0**2.0-(2.0)*b**2)

# driving parameters
f0 = 0.0         # amplitude of driving force F/m
wd = 1*w0/2         # driving frequency (will vary), book value wd=w0/5
TD = 2*np.pi/wd     # drive period, book value 1 s

print ('-----------------------------------------------------------------------')
print ('Running %s ...' % os.path.basename(__file__),)
print (' ' )
print ('Natural frequency is %0.2f rad/s' % w0)
print ('The drive frequency is %0.2f rad/s' % wd)
print ('Natural period is %0.2f s' % t0)
print ('The drive period is %0.2f s' % TD)

# Results from steady state analytic solution
def A(w):
    return f0/np.sqrt((w0**2 - w**2)**2 + (2*b*w)**2)
    
def delta(w):
    # use np.arctan2 function instead of np.arctan
    return np.arctan2(2*b*w,(w0**2 - w**2))

# Time dependent force, could be constant, cos(), sawtooth, or square
def f(t):
    return f0*np.cos(wd*t)
#    return f0*signal.square(wd*t)
#    return f0*signal.sawtooth(wd*t)
#    return f0*np.ones(np.size(t))

# functional form of differential equation to solve
def de(t, Y):
    return [Y[1], -2*b*Y[1] - w0**2*Y[0] + f(t)]

# set time range
num=5000
time_range = 60*TD   # total range time
dt = time_range/num # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array

# set frequency array for A and delta
w_range = 2*w0
dw = w_range/num 
w = (np.linspace(1,num,num)-1)*dw  # time array

# initial conditions
x0 = 0   
v0 = 0.0      
                       
# set arrays
y0= []  # array for x
y1=[]   # array for v
y0.append(x0)  # set first value for x
y1.append(v0)  # set first value for v
  
backend='dopri'  
r = ode(de)                         # define ode element
r.set_integrator(backend)          # set type of ode solver
r.set_initial_value([x0,v0], t[0])# set initial values

for tt in t[1:]:
    sol=r.integrate(tt)   # solution from ode solver
    y0.append(sol[0])    # set angle at time tt
    y1.append(sol[1])
    if not r.successful():
        print ("Warning: integration not sucessfull!")

# convert result to np type arrays for plotting 
x=np.array(y0)           
v=np.array(y1)         

plt.close('all') 

plt.figure(1)
plt.plot(w,((A(w)/A(wr))**2.0),'b', label="A(w)")
plt.xlabel('drive frequency (rad/s)')
plt.ylabel('Amplitude')
plt.title('Amplitude versus drive frequency ')
plt.grid(True)
#
#plt.figure(2)
#plt.plot(w,delta(w)/np.pi,'b', label="delta(w)")
#plt.xlabel('drive frequency (rad/s)')
#plt.ylabel('Phase (n*pi)')
#plt.title('Phase versus drive frequency ')
#plt.grid(True)
#
#plt.figure(4)
#ax1 = plt.subplot(211)
#ax1.plot(t, f(t), 'b-')
#ax1.set_ylabel('f(t)', color='b')
#ax1.tick_params('y', colors='b')
#plt.grid(True)
#plt.ylim([-1.1*f0,1.1*f0])
#plt.xlim([5 - 2*TD,5 + 2*TD])
#
#ax2 = plt.subplot(212)
#ax2.plot(t, x, 'r.')
#ax2.set_ylabel('x(t)', color='r')
#ax2.tick_params('y', colors='r')
#ax2.set_xlabel('time (s)')
#plt.xlim([5 - 2*TD,5 + 2*TD])
#
#plt.grid(True)
  
# phase space diagram 
#fig = plt.figure(10)
#ax = fig.add_subplot(111)
#ax.set_aspect(1./ax.get_data_ratio())
#plt.plot(x,v/w0, '.')
#plt.xlabel('x (radians)')
#plt.ylabel('v/w0')
#plt.title('Phase space plot')
#plt.grid(True)
 
runtime=(time.time() - start)  # stop cpu time

print (' ') 
print ('Runtime of %0.2f seconds' % runtime)