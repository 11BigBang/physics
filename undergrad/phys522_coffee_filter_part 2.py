# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 17:19:38 2015

Solve the equation of motion for drag on a coffee filter

Assume a air resistance of the form

F = eta*|v|**alpha

Fit the data measured in part 1 to a line to get alpha and beta using a linear function and 
scipy.optimize.curve_fit. Compute eta using eta = mg/exp(beta)

Solve the ODE   d(v)/dt = -g + eta/(n*m)*|v|**alpha using your values  of
alpha and eta.  Solve for n=2 and n=10 filters.  compare your computed
velocity with the data point you took.

We want to answer two questions.
1. Was the assumption that the filters attained terminal velocity “instantaneously” valid?
2. Was it a good assumption that eta is independent of the total mass of the filters?

@author: Brian Washburn
"""

import numpy as np
from scipy.integrate import ode
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import os, time

start=time.time()                   # start cpu time

# physical parameters, all in mks units
g=9.81              # gravitational acceleration near the earth
m = 1.00e-3         # mass of one coffee filter

# -----------------------------------------------------------------------------
def fit_fn (x, alpha, beta):    
    # linear fit for the data
    func = alpha*x + beta
    return func
# -----------------------------------------------------------------------------

print ('-----------------------------------------------------------------------')
print ('Running %s ...' % os.path.basename(__file__),)
print (' ' )

## load coffee filter data
## NOTE: you will need to change the filename and directory for your data!!!!
#filename='coffee_filters.txt'
#directory ='D:\\_Users\\washburn\\Classes\\24 Spring 2018\\PHYS 522 Mechanics\\03 Homework\\Homework 2\\'
#pathname=  directory + filename
#N, lnN, tdata, vdata, lnv = np.loadtxt(pathname, delimiter=',', usecols=(0,1,2,3,4), unpack=True) # load data

N = [1,2,3,4,5,6,7,8,9,10]
lnN = np.log(N)
tdata = [3.15,2.19,1.78,1.56,1.47,1.30,1.23,1.21,1.09,1.06]
vdata = [-0.95,-1.37,-1.68,-1.92,-2.04,-2.32,-2.43,-2.48,-2.75,-2.83]
vdataabs = [abs(number) for number in vdata]
lnv = np.log(vdataabs)

# fit the data ln(n) vs ln(v) to a line
# fit data using curve_fit  
popt, pcov = curve_fit(fit_fn, lnv, lnN)  # optimized coeff are in popt
#   Here    popt[0] is the fitting result for alpha
#           popt[1] is the fitting result for beta

alpha = popt[0]
beta = popt[1]
eta = m*g/np.exp(-beta)

# create new function using the fitting reults
fit2=fit_fn(lnv,alpha,beta)

# print fitting results to screen
print ('from fit: alpha = %0.3f ' % alpha)
print ('from fit: beta = %0.3f ' % beta)
print ('eta = %0.3f' % eta)

plt.close('all') 

plt.figure(1)
plt.plot(lnv,lnN,'bx',label="Data")
plt.plot(lnv,fit2,'r',label="Fit")
plt.xlabel('ln(velocity)')
plt.ylabel('ln(n)')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.grid(True)

#------------------------------------------------------------------------------
# Solve the differential equation
#   d(v)/dt = -g + eta/(N*m)*|v|**alpha 
#   
# Define
#       Y0=v
# Thus the two coupled first order DE are
#       d(Y0)/dt = -g + eta/(n*m)*|v|**alpha 1

# functional form of differential equation
def de(t, Y, n):
    return -g + eta/(n*m)*np.abs(Y[0])**alpha 

## initial conditions
num=1000
time_range = 3.0   # total range time
dt = time_range/num # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array
#
# initial conditions
Y00 = 0.0     # start from rest                 

#-----------------------------------------------------------------------------
# solve for N = 2 coffee filters

# set solution array
y0= []  # array for angle
y0.append(Y00)  # set first value for angle

backend='dopri'  
r = ode(de)                         # define ode element
r.set_integrator(backend)          # set type of ode solver
r.set_initial_value(Y00, t[0])# set initial values
r.set_f_params(2)  # set number of filters n = 2
#
for tt in t[1:]:
    sol=r.integrate(tt)   # solution from ode solver
    y0.append(sol[0])    # set angle at time tt
    if not r.successful():
        print ("Warning: integration not sucessfull!")

# convert result to np type arrays for plotting 
v=np.array(y0)            # angle solution 

# data values for n=2 filters
# this is the measured time and velocity for the n=2 run
#  NOTE: you need to put in your experimental values here
t2 = tdata[1]
v2 = vdata[1]

# plot the numerical answer with your one data point at (t2,v2)
plt.figure(2)
plt.plot(t,v,'b', label="solution")
plt.plot(t2,v2,marker='o',markersize=5,color='red',label='data')  
plt.xlabel('time (seconds)')
plt.ylabel('velocity (m/s)')
plt.title('Velocity versus time for n=2 filters')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.grid(True)

#-----------------------------------------------------------------------------
# solve for n = 10 coffee filters

y0= []  # array for angle
y0.append(Y00)  # set first value for angle
r.set_initial_value(Y00, t[0])# set initial values
r.set_f_params(10)  # set number of filters n = 10
#
for tt in t[1:]:
    sol=r.integrate(tt)   # solution from ode solver
    y0.append(sol[0])    # set angle at time tt
    if not r.successful():
        print ("Warning: integration not sucessfull!")

# convert result to np type arrays for plotting 
v=np.array(y0)            # angle solution 

# data values for N=10 filters
# this is the measured time and velocity for the n=10 run
t10 = tdata[9]
v10 = vdata[9]

# plot the numerical answer with your one data point at (t10,v10)
plt.figure(3)
plt.plot(t,v,'b', label="solution")
plt.plot(t10,v10,marker='o',markersize=5,color='red',label='data')
plt.xlabel('time (seconds)')
plt.ylabel('velocity (m/s)')
plt.title('Velocity versus time for n=10 filters')
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)
plt.grid(True)

runtime=(time.time() - start)  # stop cpu time
print (' ') 
print ('Runtime of %0.2f seconds' % runtime)