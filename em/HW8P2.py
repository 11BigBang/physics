import numpy as np

freqs = [1*10**3, 1*10**6, 300*10**6, 1*10**9, 10*10**9, 30*10**9, 100*10**9]
mu = 4*np.pi*10**(-7)

elements = {
    'aluminum':
            {
                'sigma': 3.5 * 10**7,
                'skin pens': [],
                'impedances': []
            },
    'copper':
            {
                'sigma': 5.96 * 10**7,
                'skin pens': [],
                'impedances': []
            },
    'silver':
            {
                'sigma': 6.30 * 10**7,
                'skin pens': [],
                'impedances': []
            },
    'graphene':
            {
                'sigma': 1.00 * 10**8,
                'skin pens': [],
                'impedances': []
            }
    }

for element in elements:
    for freq in freqs:
        elements[element]['skin pens'].append(round((2 /(freq * 2 * np.pi * mu * elements[element]['sigma']))**(0.5), 8))
        elements[element]['impedances'].append(round(((mu * freq * 2 * np.pi) / (2 * elements[element]['sigma']))**(0.5), 8))

for element in elements:
    print(elements[element]['skin pens'], '  ', elements[element]['impedances'], '(1+j)')