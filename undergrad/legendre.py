# -*- coding: utf-8 -*-

from sympy import *
from scipy import *
from matplotlib import pyplot as plt
import numpy as np

init_printing(use_unicode=True)
# init_session(quiet=True)
from sympy.simplify.radsimp import collect_sqrt

x = Symbol('x')
l = 3
m = -1*l
mlist = []

while m <= l:
    mlist.append(m)
    m += 1
        
xvals = np.linspace(0,2*pi,1000)
y = [1]*1000

# ans = legendre(l,x)
# pprint(simplify(ans))
# pprint(np.roots([63/8,0,-35/4,0,15/8,0]))

# plt.figure(1)
# plt.title('Legendre N = 5')
# plt.plot(x1,y)

for i in mlist:
    print('P of l=',l,' and m=',mlist[i])
    print('COPYABLE:  ',simplify(assoc_legendre(l,mlist[i],x)))
    pprint(simplify(assoc_legendre(l,mlist[i],x)))
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#Plots specifically for all m values in Legendre of l = 3    
plt.figure(1)
plt.polar(xvals,3*(1 - 5*cos(xvals)**2)*sqrt(1 - cos(xvals)**2)/2)
plt.axis(ymin = 0)
plt.legend(title = 'P of l= 3  and m= 1')

plt.figure(2)
plt.polar(xvals,15*cos(xvals)*(1 - cos(xvals)**2))
plt.axis(ymin = 0)
plt.legend(title = 'P of l= 3  and m= 2')

plt.figure(3)
plt.polar(xvals,-15*(1 - cos(xvals)**2)**(3/2))
plt.axis(ymin = 0)
plt.legend(title='P of l= 3  and m= 3')

plt.figure(4)
plt.title('P of l= 3  and m= -3')
plt.polar(xvals,(1 - cos(xvals)**2)**(3/2)/48)
plt.axis(ymin = 0)
plt.legend(title='P of l= 3  and m= -3')

plt.figure(5)
plt.polar(xvals,cos(xvals)*(1 - cos(xvals)**2)/8)
plt.axis(ymin = 0)
plt.legend(title='P of l= 3  and m= -2')

plt.figure(6)
plt.polar(xvals,sqrt(1 - cos(xvals)**2)*(5*cos(xvals)**2 - 1)/8)
plt.axis(ymin = 0)
plt.legend(title='P of l= 3  and m= -1')

plt.figure(7)
plt.polar(xvals,cos(xvals)*(5*cos(xvals)**2 - 3)/2)
plt.axis(ymin = 0)
plt.legend(title='P of l= 3  and m= 0')
