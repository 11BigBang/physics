# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 06:32:14 2020

@author: wbmar
"""
#website for high order bessel https://www.sciencedirect.com/topics/mathematics/spherical-bessel-function

from sympy import *
from scipy.optimize import root
import numpy as np
from matplotlib import pyplot as plt

x = Symbol('x',real=True)
# r = Symbol('r',real=True)
# k = Symbol('k',real=True)
# n = Symbol('n',real=True)
# u = Function('u')(r)
l = 4

if l == 0:
    bessel = (((-1*x)**(l))/(x**l))*sin(x)/x
    neuman = -1*(((-1*x)**(l))/(x**l))*cos(x)/x
elif l == 1:
    bessel = (((-1*x)**(l))/(x**l))*diff(sin(x)/x,x)
    neuman = -1*(((-1*x)**(l))/(x**l))*diff(cos(x)/x,x)
elif l == 2:
    bessel = ((-1*x)**l)*(1/x)*diff((1/x)*diff(sin(x)/x,x),x)
    neuman = -1*(((-1*x)**(l))/(x**l))*diff(cos(x)/x,x,x)
elif l == 3:
    bessel = ((-1*x)**l)*(1/x)*diff((1/x)*diff((1/x)*diff(sin(x)/x,x),x),x)
    neuman = -1*(((-1*x)**(l))/(x**l))*diff(cos(x)/x,x,x,x)
elif l == 4:
    bessel = ((-1*x)**l)*(1/x)*diff((1/x)*diff((1/x)*diff((1/x)*diff(sin(x)/x,x),x),x),x)
    neuman = -1*(((-1*x)**(l))/(x**l))*diff(cos(x)/x,x,x,x,x)
else:
    bessel = 'error'
    
# r = np.linspace(0, 10,1000) 
# soln = roots(r-np.tan(r),guess)
# print(soln.r)

    
print('j',l,'    COPYABLE: ',simplify(bessel))
print('')
pprint(simplify(bessel))
print('ooooooooooooooooooooooooooooooooooo')
print('n',l,'    COPYABLE: ',neuman)
print('neuman is probably wrong value')
pprint(neuman)
print('ooooooooooooooooooooooooooooooooooo')
# pprint(simplify(ans))
# pprint(jn_zeros(1,1))




