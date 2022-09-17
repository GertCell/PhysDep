# Метод простых итераций

from numpy import *

# Function real root is 1.386

#m = 9.1 * 10 ** (-31)
#U = 1.6*10**(-18)
#h = 1.05 * 10 ** (-34)
#a_b = 0.5 * 10 ** (-10)

c_0 = 20


def f(x):
    # c_0 = (2*m*(a_b**2)*U)/(h**2)
    print(c_0)
    return 1 / (tan(sqrt(c_0*abs(1 - x)))) - sqrt(abs(1 / x - 1))


a = 0.2
b = 0.35
N = 200000
X = []
D = []
k = 1e-12


def method():
    x0 = (a + b) / 2
    xn = f(x0)
    xn1 = xn - 0.1 * f(xn)
    for i in range(0, N):
        if abs(xn1 - xn) > k:
            xn = xn1
            xn1 = xn - 0.1 * f(xn)
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
