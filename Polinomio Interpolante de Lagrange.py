# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Métodos Numéricos
Sección 40
Sergio Alejandro Vasquez Marroquin - 161259
20/07/2023

POLINOMIO INTERPOLANTE DE LAGRANGE
"""

from pylab import *
from tabulate import tabulate
from scipy.interpolate import lagrange

x = [0,1,2,3,4,5]
y = [3.88578E-16,-1.88738E-15,4.88498E-15,-3.55271E-15,1,0]

f = lagrange(x, y)

print(f(0.85))


# HT 6 - PROB 2
# x = [0,1,2,5.5,11,13,16,18]
# y = [0.5,3.134,5.3,9.9,10.2,9.35,7.2,6.2]
# print(f(8))

# HT6 - PROB 4.1
# x = [0,1,2,3,4,5]
# y = [-0.002036199,0.026244344,-0.106561086,0.066515837,0.515837104,0]
# print(f(0.85))

# HT6 - PROB 4.2
# x = [0,1,2,3,4,5]
# y = [3.88578E-16,-1.88738E-15,4.88498E-15,-3.55271E-15,1,0]
# print(f(0.85))


