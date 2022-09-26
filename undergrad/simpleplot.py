# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Python code
#Author: Bryant Martin

from matplotlib import pyplot as plt
import numpy as np

# setting the x - coordinates 
x = np.linspace(0, 10,100000) 
y = 1

# setting the corresponding y - coordinates 
#even1 = np.tan(z)
#even2 = np.sqrt((64/z**2)-1)
#odd1 = 1/np.tan(z)
#odd2 = -1 * np.sqrt((64/z**2)-1)
#  
#
## plotting the points
#plt.figure(1) 
#plt.plot(z, even1, label= 'tan(z)')
#plt.plot(z, even2, label= 'sqrt((64/z**2)-1)') 
#plt.text(1.395,np.sqrt((64/1.395**2)-1),'n=1')
#plt.text(4.165,np.sqrt((64/4.165**2)-1),'n=3')
#plt.text(6.831,np.sqrt((64/6.831**2)-1),'n=5')
#plt.xlabel('z')
#plt.xlim(0,10)
#plt.ylim(0,10)
#plt.ylabel('Functions')
#plt.title('Finite Square Well')
#plt.legend()
#
## plotting the points 
#plt.figure(2)
#plt.plot(z, odd1, label= 'cot(z)')
#plt.plot(z, odd2, label= '-sqrt((64/z**2)-1)') 
#plt.text(2.786,-1*np.sqrt((64/2.786**2)-1),'n=2')
#plt.text(5.521,-1*np.sqrt((64/5.521**2)-1),'n=4')
#plt.text(7.957,-1*np.sqrt((64/7.857**2)-1),'n=6')
#plt.xlabel('z')
#plt.xlim(0,10)
#plt.ylim(-10,0)
#plt.ylabel('Functions')
#plt.title('Finite Square Well')
#plt.legend()
#  

## function to show the plot 
#plt.show(2) 
y1 = -1*(np.cos(x)/np.sin(x))
y2 = np.sqrt((25.938*3*np.pi/4)/x**2-1)
# plotting the points
plt.figure(1) 
plt.plot(x, y1, label= '-cotan(z)')
plt.plot(x, y2, label= 'sqrt((z0/z)**2-1)')
plt.axvline(x=np.pi/2,label='pi/2',color='red',linestyle='dashed')
# plt.yticks(np.linspace(0, 10,1))
#plt.plot(x, y, label='Potential') 
plt.xlabel('x')
plt.xlim(0,10)
plt.ylim(0,5)
plt.ylabel('Functions')
plt.title('Spherical Well')
plt.legend()