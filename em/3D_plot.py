import numpy as np
import matplotlib.pyplot as plt


ax = plt.figure().add_subplot(projection='3d')

# Prepare arrays x, y, z
z = np.linspace(-1, 1, 1000)
x = z*0
y = z*0

ax.plot(x, y, z, label='parametric curve')

ax.legend()

plt.show()