import matplotlib.pyplot as plt
import numpy as np

# Set up time intervals and declare constants
wl1 = np.linspace(10**(-10), 4*10**(-6), 1000)   # Frequency 1000 THz
wl2 = np.linspace(10**(-10), 8*10**(-5), 1000)   # Frequency 100 THz
wl1_um = wl1 * 10**6                            # Wavelengths in microns
wl2_um = wl2 * 10**6                            # Wavelengths in microns

c = 3.0 * 10**8                                 # Speed of light in vacuum                                     # Wavelength in meters
h = 6.62618 * 10**(-34)                         # Planck's constant
k = 1.38 * 10**(-23)                            # Boltzmann's constant
A = 2897.777                                    # Wein's constant in um K

def spectrum(T, wl):
    return (8*np.pi*h*c)/wl**5 / (np.exp((h*c)/(wl*k*T))-1)

def peak_wl(T):
    return A/T

# Wide range of temperatures
rho3033 = spectrum(3033, wl1)   # 3033 K
rho4422 = spectrum(4422, wl1)   # 4422 K
rho5811 = spectrum(5811, wl1)   # Sun temperature: 5811 K

rho3033_peak = peak_wl(3033)   # Peak wavelength at 3033 K
rho4422_peak = peak_wl(4422)   # Peak wavelength at 4422 K
rho5811_peak = peak_wl(5811)   # Peak wavelength at 5811 K

# Near room temperature objects
rho273 = spectrum(273, wl2) # 0 degrees Celsius
rho294 = spectrum(294, wl2) # Room temperature: 294 K, 21 C, 70 F
rho306 = spectrum(306, wl2) # Skin temperature: 306 K, 33 C, 91 F

rho273_peak = peak_wl(273) # Peak wavelenngth at 0 C
rho294_peak = peak_wl(294) # Peak wavelength at 294 K
rho306_peak = peak_wl(306) # Peak wavelength at 306 K

plt.style.use('bmh')

# Plots
fig1, ax1 = plt.subplots()
# plt.title("Planck's Spectral Distribution")
plt.xlabel("Wavelength (microns)")
plt.ylabel("Photon Density")
ax1.plot(wl1_um, rho3033, label='5000 F')
ax1.plot(wl1_um, rho4422, label='7500 F')
ax1.plot(wl1_um, rho5811, label='Surface of Sun: 10,000 F')
plt.vlines(x=rho3033_peak, ymin=0, ymax=np.nanmax(rho3033), color='b', linestyle=(0,(1,1)))
plt.vlines(x=rho4422_peak, ymin=0, ymax=np.nanmax(rho4422), color='r', linestyle=(0,(1,1)))
plt.vlines(x=rho5811_peak, ymin=0, ymax=np.nanmax(rho5811), color='purple', linestyle=(0,(1,1)))
plt.legend()
plt.show()

fig2, ax2 = plt.subplots()
# plt.title("Planck's Spectral Distribution")
plt.xlabel("Wavelength (microns)")
plt.ylabel("Photon Density")
ax2.plot(wl2_um, rho273, label='FP of water: -32 F')
ax2.plot(wl2_um, rho294, label='Room Temp: 70 F')
ax2.plot(wl2_um, rho306, label='Skin Temp: 91 F')
plt.vlines(x=rho273_peak, ymin=0, ymax=np.nanmax(rho273), color='b', linestyle=(0,(1,1)))
plt.vlines(x=rho294_peak, ymin=0, ymax=np.nanmax(rho294), color='r', linestyle=(0,(1,1)))
plt.vlines(x=rho306_peak, ymin=0, ymax=np.nanmax(rho306), color='purple',linestyle=(0,(1,1)))
plt.legend()
plt.show()
