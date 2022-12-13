# Дихотемия

from numpy import *


m = 9.1 * 10 ** (-31)
U = 1.6*10**(-18)
h = 1.05 * 10 ** (-34)
a_b = 0.5 * 10 ** (-10)


def root():

    def f(x):
        c_0 = 1
        return x**2 - 4


    print('write precision (k) and max number of iterations (n)')
    k = float(input())
    n = int(input())

    a = 0

    b = 10


    if f(a) * f(b) < 0:
        for i in range(1, n):

            if f((a + b) / 2) * f(b) < 0:
                a = (a + b) / 2
            else:
                b = (a + b) / 2
            print('current number of iterations =', i, (a + b) / 2)


    else:

        print('change range or function has not any roots')
    print('root =', (a + b) / 2)


root()
