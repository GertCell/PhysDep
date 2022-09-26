# Trapezoid

from scipy import *
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
# Function


def f(x):
    return 1 / (x ** 2 + 1)


# Real solution

v = np.pi/2
print('real value', v)

# Parameters

a = 1
b = -1

# Segment splitting

n = 100
d = (b-a)/n
S1 = []
S2 = []


def trapz():
    xi = a
    xi_1 = xi + d
    s1 = (f(xi_1) + f(xi)) * d
    for i in range(0, n - 1):
        xi = xi_1
        xi_1 = xi + d
        s = s1
        s1 = s + (f(xi_1) + f(xi)) * d
        S1.append(v + s1/2)
    print('Trapz result', -s1/2)
    return S1


def simpson():
    xi = a
    xi_1 = xi + d
    xi_2 = xi_1 + d
    s1 = d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
    for i in range(0, n-1):
        xi = xi_1
        xi_1 = xi + d
        xi_2 = xi_1 + d
        s = s1
        s1 = s + d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
        S2.append(v + s1/2)
    print('Simpson result', -s1/2)
    return S2


trapz()
simpson()

y = np.arange(0, 99)

plt.plot(y, S1, 'r--', y, S2, 'r--')
# ax[1].plot(S2)

plt.show()

