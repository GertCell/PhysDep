# Newton

from numpy import *

m = 9.1 * 10 ** (-31)
U = 1.6*10**(-18)
h = 1.05 * 10 ** (-34)
a_b = 0.5 * 10 ** (-10)
#c_0 = (2 * m * (a_b ** 2) * U) / (h ** 2)*1
c_0 = 20

# Function
def f(x):
    return 1 / (tan(sqrt((c_0 * (1 - x))))) - sqrt(1 / x - 1)


# Derivative
def f1(x):
    return c_0 / (2 * sqrt(1 - x) * (sin(c_0*sqrt(1 - x))) ** 2 ) + 1 / (
                2 * x ** 2 * (sqrt((1 / x - 1))))


a = 0.1
b = 0.4
N = 200
X = []
D = []
k = 0.0001


def method():

    x0 = (a + b) / 2
    xn = x0
    xn1 = xn - f(xn) / f1(xn)

    for i in range(0, N):
        if abs(xn1 - xn) > k:
            xn = xn1
            xn1 = xn - f(xn) / f1(xn)
            D.append(xn1 - xn)
            X.append(xn1)

        else:
            print('preferred precision', k)
            print('current precision', "%.5f" % D[i - 2])
            print('current number of iteration', i - 1)
            print('root', "%.5f" % X[i - 2])
            break
    return 0


method()
