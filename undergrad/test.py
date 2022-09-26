for j in range(7):
        # -*- coding: utf-8 -*-
    """
    Created on Fri Dec 25 17:19:38 2015
    
    Solve the equation of motion for projectile motion with air resistance of the 
    form
    
    F_air = c*v**2 (in the - v_hat direction)
    
    Do this for a baseball of mass m and diameter d.  The air resistance will 
    be given by 
    
    c = gamma*d**2
    
    where gamma is coeffiecient for spherical objects (Taylor page 45)
    
    Uses the more complex class structure of ode, specifically Runge-Kutta 4/5 
    algorithm called 'dopri5'
    
    The last line plots a movie of the two trajectories using animate_trajectory()
    
    @author: Brian Washburn
    """
    import numpy as np
    from scipy.integrate import ode
    from matplotlib import pyplot as plt
    from scipy import interpolate
    import os, time
    ##import phys522 as phys              # import phys522 module
    
    start=time.time()                   # start cpu time
    
    # physical parameters, all in mks units
    g = 9.81             # gravitational acceleration near the earth
    d = 0.229            # ball diameter
    gamma = 0.25         # coefficient of quadratic air resistance
    m = 4.536            # ball mass
    vterm = np.sqrt(m*g/(gamma*d**2))  # terminal speed
    c =gamma*d**2        # quadtratic force coefficient c
    
    print ('-----------------------------------------------------------------------')
    print ('Running %s ...' % os.path.basename(__file__),)
    print (' ' )
    #
    # Define coupled 1st order differential equations from Taylor page 62
    # The equation of motion has the form
    # d(vx)/dt = -(c/m)*sqrt(vx**2 + vy**2)*vx
    # d(vy)/dt = -g - (c/m)*sqrt(vx**2 + vy**2)*vy   
    #
    # Define
    #       Y0=vx
    #       Y1=vy
    #
    #------------------------------------------------------------------------------
    def de(t, Y):
        return [-(c/m)*np.sqrt(Y[0]**2 + Y[1]**2)*Y[0], \
        -g - (c/m)*np.sqrt(Y[0]**2 + Y[1]**2)*Y[1]   ] 
    
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
    
    #------------------------------------------------------------------------------
    
    # initial conditions
    num=100000
    TF = 5.0        # total time in seconds
    dt = TF/num     # time increment
    t = (np.linspace(1,num,num)-1)*dt  # time array
    
    #initial velocity conditions
    x00 = 0.0    # inital position x
    y00 = 2.01   # initial position y
    v0 = 10.0   # initial speed
    theta = float((j*5)+30)*np.pi/180 # initial angle in radians
    vx0 = v0*np.cos(theta) # initial vx
    vy0 = v0*np.sin(theta) # initial vy
    Y00 = vx0
    Y10 = vy0
    
    # set arrays
    y0= []  # array for angle
    y1=[]   # array for angular speed
    y0.append(Y00)  # set first value for angle
    y1.append(Y10)  # set first value for angular speed
      
    backend='dopri'  
    r = ode(de)                         # define ode element
    r.set_integrator(backend)          # set type of ode solver
    r.set_initial_value([Y00,Y10], t[0])# set initial values
    
    for tt in t[1:]:
        sol=r.integrate(tt)   # solution from ode solver
        y0.append(sol[0])    # set angle at time tt
        y1.append(sol[1])
        if not r.successful():
            print ("Warning: integration not sucessfull!")
    
    # convert result to np type arrays for plotting 
    vx=np.array(y0)            
    vy=np.array(y1)    
    
    # find intianeous position by direct integration
    x = np.cumsum(vx)*dt + x00
    y = np.cumsum(vy)*dt + y00  
    
    idx, tmax = solve_eq(t,vy,0,0,3)
    print ('The max height of %0.3f occurs at %0.3f s.' %(y[idx],tmax))
    
    idx, tmax = solve_eq(t,y,0,0,10)
    print ('The ball crosses 0 at %0.3f occurs at %0.3f s.' %(x[idx],tmax))
    
    # No air resistance solution
    xno = x00 + vx0*t
    yno = y00 + vy0*t - 0.5*g*t**2
    
    idx, tmax = solve_eq(t,yno,0,0,10)
#    print ('With no air resistance the ball crosses 0 at %0.3f occurs at %0.3f s.' %(xno[idx],tmax))
#     
#    plt.close('all') 
#     
#    plt.figure(1)
#    plt.plot(t,x,'b')
#    plt.xlabel('time (seconds)')
#    plt.ylabel('horizontal position (m')
#    plt.title('x vs time')
#    plt.grid(True)
#      
#    plt.figure(2)
#    plt.plot(t,y,'b')
#    plt.xlabel('time (seconds)')
#    plt.ylabel('verticle position (m')
#    plt.title('y vs time')
#    plt.grid(True)
    
    fig = plt.figure(3,figsize=(15,6))
    ax = fig.add_subplot(111)
    ax.set_aspect(1./ax.get_data_ratio())
    plt.plot(x,y, label=(((j*5)+30)))
#    plt.plot(xno,yno,'b', label="No air resistance")
    plt.xlabel('Horizontal Position (meters)')
    plt.ylabel('Vertical Position (meters)')
    plt.title('Trajectory')
    plt.xlim([0,15])
    plt.ylim([0,6])
    
    plt.legend(title=('Angle'))
    plt.grid(True)
    
    ## make an animation of trajectory
    #mkani = True
    #if mkani == True:
    #    progn = os.path.basename(__file__)[0:-3]
    #    phys.animate_trajectories(dt,x,y,xno,yno,progn)
    
    runtime=(time.time() - start)  # stop cpu time
    
