# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:13:33 2019

@author: wbmar
"""

import numpy as np

N = 10000
onect = 0
twoct = 0
threect = 0
fourct = 0
fivect = 0
sixct = 0

for i in range (0, N):
    x = np.random.randint(1,7)
    if x == 1:
        onect += 1
    elif x == 2:
        twoct += 1
    elif x == 3:
        threect += 1
    elif x == 4:
        fourct += 1
    elif x == 5:
        fivect += 1
    elif x == 6:
        sixct += 1
    else:
        print('something went wrong')

print('Number of 1s:')
print(onect)
print('Number of 2s:')
print(twoct)
print('Number of 3s:')
print(threect)
print('Number of 4s:')
print(fourct)
print('Number of 5s:')
print(fivect)
print('Number of 6s:')
print(sixct)