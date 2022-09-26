"""Johns Hopkins University - MS Applied Physics; Module 7 Assignment, Problem 3

Using MATLAB, Excel, etc. plot the Planck Distribution Blackbody curves for 300K, 400K, 500K,
600K.
"""

import matplotlib.pyplot as plt
import numpy as np

class PlanckDistribution:
    def __init__(self, Ts):
        self.h = 6.626068 * 10 ** (-34)  # Planck's Constant (m**2 kg s**-1)
        self.k_b = 1.380649 * 10 ** (-23)  # Boltzmann's Constant (J/K)
        self.c = 2.99792458 * 10 ** (8)  # Speed of light (m/s)
        self.w = 2.898 * 10 ** (-3)  # Wien Displacement Constant (mK)
        self.all_lambdas = np.linspace(0.0000000001, 100 * 10 ** (-6), 1000)
        self.Ts = Ts
        self.master_list = []

        for T in Ts:
            #Each item is list will be list [lambdas, L, T, peak_lambda, peak_radiance]
            self.master_list.append(self.create_data(T))

    def find_radiance(self, wavelength, T):
        return 2 * self.h * self.c ** 2 / ((wavelength ** 5) * (np.exp(self.h * self.c / (wavelength * self.k_b * T)) - 1))

    def create_data(self, T):
        lambdas = self.all_lambdas
        L = self.find_radiance(lambdas, T)
        peak_lambda = self.w/T
        peak_radiance = self.find_radiance(peak_lambda, T)

        #Deletes unimportant data
        l, to_delete = 0, []
        while l < len(L):
            if L[l] < 0.01*peak_radiance:
                to_delete.append(l)
            l += 1
        to_delete.reverse()

        for i in to_delete:
            lambdas = np.delete(lambdas, i)
            L = np.delete(L, i)

        return lambdas, L, T, peak_lambda, peak_radiance

    def graph_distro(self):
        #Show graphically
        plt.style.use('bmh')
        fig, ax = plt.subplots()
        for data in self.master_list:
            ax.plot(data[0], data[1], label=f'{data[2]}K')
            ax.text(data[3], data[4], f'{round(data[3]*10**6, 9)} microns')
        plt.title('Planck Distribution')
        plt.xlabel('Wavelength (m)')
        plt.ylabel('Radiance (L)')
        plt.legend()
        plt.show()

    def print_peaks(self):
        for data in self.master_list:
            print(f'The peak for temperature {data[2]}K is {data[3]} meters.')

pd = PlanckDistribution([300, 400, 500, 600])
pd.graph_distro()
pd.print_peaks()