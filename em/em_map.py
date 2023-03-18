import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)

X,Y = np.meshgrid(x,y)



Ex = (X + 1)/((X + 1)**2 + Y**2) - (X - 1)/((X - 1)**2 + Y**2)
Ey = Y/((X + 1)**2 + Y**2) - Y/((X - 1)**2 + Y**2)

fig, ax = plt.subplots()
strm = ax.streamplot(X,Y,Ex,Ey,color=Ey, linewidth=1, cmap='autumn')
fig.colorbar(strm.lines)
ax.set_title("EM")

plt.show()

