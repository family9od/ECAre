# -*- coding: utf8 -*-
"""
simple demo of the fill function
"""

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 1, 500)

y = np.sin(10 * 2* np.pi * x ) * np.exp(-5 * x)

plt.fill(x, y, 'r')
plt.grid(True)

plt.show()
