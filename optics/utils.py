import numpy as np

def snell_theta_t(ni, nt, theta_i):
    """Uses Snell's Law to calculate the transmission angle."""
    return np.arcsin(ni * np.sin(theta_i) / nt)

def thin_lens_t1(t0, f):
    """Uses the Thin Lens Equation to calculate the image location.
    It is important to remember that t0 needs to be negative if it is to the left of the lens."""
    return (t0 * f) / (t0 + f)

def lensmaker(n, R1, R2, f):
    """Returns the focal length (f) of a lens given the lens' index of refraction (n), and each side's
    radius of curvature (R1 and R2)"""
    return 1 / ((n - 1) * ((1 / R1) - (1 / R2)))