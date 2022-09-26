# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:06:40 2020

@author: wbmar
"""
#using 'pprint' will print in a pretty way
#eulers number will be displayed as E since you imported this
#pprint(expand(whatever)) will multiply binomials for example
#print(simplify(whatever)) will simplify sin(x)*cos(x) to sin(2*x)/2 for example
#because from sympy you imported * or all of the package you don't have to use to sympy. part
#double o (oo) is interpreted as infinity
#integrate((function), (with respect to, lower limit, upper limit))
#example:  integrate(sp.sin(n*pi*x/a)*A*x*(x-a), (x, 0, a))

# use the form below to ensure positive, real answers if the answer seems strange
#z = Symbol('z',real=True,positive=True)

from sympy import *

init_printing(use_unicode=True)
from sympy.simplify.radsimp import collect_sqrt

H = Symbol('H')
a = Symbol('a')
C = Symbol('C')
t = Symbol('t')
r = Symbol('r',real=True,positive=True)
c = Symbol('c')
A = Symbol('A',real=True,positive=True)
x = Symbol('x')
k = Symbol('k',real=True,positive=True)

# pprint(sqrt(C*a+a**2))
# pprint(simplify(integrate(1/sqrt(C*a+a**2),a)))
pprint(trigsimp((2*sqrt(a)*sqrt(a+C)*ln(sqrt(a)+sqrt(a+C)))/sqrt(a*(a+C))))


#i = Symbol('i')
#k = Symbol('k')
#a = Symbol('a')
#b = Symbol('b')
#B = Symbol('B')

#print(simplify(solve(((b*exp(-i*k*a)+b*B*exp(i*k*a))/sin(b*a))+i*k*exp(-i*k*a)-i*k*B*exp(i*k*a), B)))


