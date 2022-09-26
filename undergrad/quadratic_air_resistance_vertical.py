# -*- coding: utf-8 -*-
"""
Solve the equation of motion for 1 D vertical motion with air resistance of the 
form

F_air = c*v**2 (in the - v_hat direction)

Do this for a baseball of mass m and diamater d.  The air resistance will 
be given by 

c = gamma*d**2

where gamma is coeffiecient for spherical objects (Taylor page 45)

@author: Brian Washburn
"""
import numpy as np
from scipy.integrate import ode
from scipy import interpolate 
from matplotlib import pyplot as plt
import os, time

start=time.time()                   # start cpu time

# physical parameters, all in mks units
g = 9.81             # gravitational acceleration near the earth
d = 0.07             # ball diameter
gamma = 0.25         # coefficient of quadratic air resistance
m = 0.15             # ball mass
vterm = np.sqrt(m*g/(gamma*d**2))  # terminal speed
c =gamma*d**2        # quadtratic force coefficient c
tau = vterm/g
t98 = 2.3*tau
print ('-----------------------------------------------------------------------')
print ('Running %s ...' % os.path.basename(__file__),)
print (' ')
print (' ')
print ('The terminal speed is %0.3f m/s' % vterm)

#
# Solve 1D motion
# The equation of motion has the form
# d(vy)/dt = g*(1 - np.sign(Y[0])*(Y[0]/vterm)**2)
#
# where np.sign(Y[0]) gives me the sign (+1 or -1) of Y[0]
#
# this is needed to get the correct direction of the air resistant force for 
# vy < 0 (the square term removes correct sign)

#------------------------------------------------------------------------------
#without negative velocity (upward motion)
#def de(t, Y):
#    return g*(1 - np.sign(Y[0])*(Y[0]/vterm)**2)
#------------------------------------------------------------------------------
#when velocity is negative as stated 2 segments above
def de(t, Y):
    return g*(1 - np.sign(Y[0])*(Y[0]/vterm)**2)
#------------------------------------------------------------------------------

def solve_eq(t,f,a,ti,tf):
    # for the function f(t) solve the equation for T where f(T)==a 
    # in the range ti<t<tf
    # To do this
    #   1) Create an interpolation function fint from f - a using a cublic spline
    #   2) Find the roots of spline function, i.e. f - a = 0 or fint = 0
    idxi = (np.abs(t-ti)).argmin()  # closest index for value ti
    idxf = (np.abs(t-tf)).argmin()  # closest index for value tf
    tc = t[idxi:idxf] # concatenate t and f
    fc = f[idxi:idxf]
    fint = interpolate.splrep(tc,fc-a,s=0)   # cubic spline function f
    roots = interpolate.sproot(fint)       # find the roots of f
    T = roots[0]
    idxT = (np.abs(t-T)).argmin()  # index of solution
    return idxT, T

# initial conditions
num=100
TF = 10.0        # total time in seconds
dt = TF/num     # time increment
t = (np.linspace(1,num,num)-1)*dt  # time array

# initial velocity conditions
vy0 = -1.5*vterm   # initial speed

# set solution array
y0= []  # solution array for vy

y0.append(vy0)  # set initial value
  
backend='dopri'  
r = ode(de)                         # define ode element
r.set_integrator(backend)          # set type of ode solver
r.set_initial_value(y0[0], t[0])# set initial values

for tt in t[1:]:
    sol=r.integrate(tt)   # solution from ode solver
    y0.append(sol[0])    # set angle at time tt
    if not r.successful():
        print ("Warning: integration not sucessfull!")

# convert result to np type arrays for plotting 
vy=np.array(y0)            

# find heigh by direct integration
y = np.cumsum(vy)*dt

 
# find the time from the object to go up then down
idx, ts = solve_eq(t,y,0,0,10.0)
print ('The time for the ball to go up and then back down to y=0 is %0.3f s' % ts) 

idx, tmax = solve_eq(t,vy,0,3,10)
print ('The max height of %0.3f occurs at %0.3f s.' %(y[idx],tmax))

#idx, t98 = solve_eq(t,vy,34.3,0,1000)
#print ('The ball reaches 98 percent of its terminal velocity at %0.3f s' % t98)

print ('The time to reach 98 percent terminal velocity is 2.3 times tau or %0.3f s' % t98)

plt.close('all') 
 
plt.figure(1)
plt.plot(t,vy,'b', label= 'Runge-Kutta Solution')
plt.plot(t,vterm*np.ones(num),'g',label= 'vterm')
plt.xlabel('time (seconds)')
plt.ylabel('vertical speed (m/s)')
plt.title('vy vs time')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)

plt.figure(2)
plt.plot(t,y,'r', label= 'Runge-Kutta Solution')
plt.xlabel('time (seconds)')
plt.ylabel('height (m)')
plt.title('y vs time')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=0, borderaxespad=0.)

runtime=(time.time() - start)  # stop cpu time
print (' ')
print ('Runtime of %0.2f seconds' % runtime)
