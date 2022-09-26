"""Johns Hopkins University - MS Applied Physics; Module 4 Assignment, Problem 1B

Determines numerically the minimum distance between object and real image on either
side of a thin lens.
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')

f = 50

#Create list of t0 values that will yield only real images and find t0-t1
t0 = np.linspace(-5*f, -1*f-1, 1000)
t1 = t0*f/(t0+f)
delta_ts = t1 - t0

#Find the minimum separation of t0 and t1
min_delta = min(delta_ts)
min_index = np.where(delta_ts==min_delta)
min_t0 = t0[min_index]

print(f'The minimum difference between is at approximately {min_delta/f}f.')

#Show graphically
fig, ax = plt.subplots()
ax.plot(t0, delta_ts, label='f=50')
plt.xlabel('t0')
plt.ylabel('t0-t1')
plt.legend()
plt.show()
