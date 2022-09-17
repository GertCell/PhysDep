# Trapezoid

from scipy import *

# Function


def f(x):
    return 1 / (x ** 2 + 1)


# Real solution

v = integrate.quad(f, -1, 1)
print('real value', v)

# Parameters

a = 1
b = -1

# Segment splitting

n = 100
d = (b-a)/n


def trapz():
    xi = a
    xi_1 = xi + d
    s1 = (f(xi_1) + f(xi)) * d
    for i in range(0, n - 1):
        xi = xi_1
        xi_1 = xi + d
        s = s1
        s1 = s + (f(xi_1) + f(xi)) * d
    print('Trapz result', -s1/2)


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
    print('Simpson result', -s1/2)


trapz()
simpson()
