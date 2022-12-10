# Дихотемия

from numpy import *


m = 9.1 * 10 ** (-31)
U = 1.6*10**(-18)
h = 1.05 * 10 ** (-34)
a_b = 0.5 * 10 ** (-10)


def root():

    def f(x):
        c_0 = 1
        return 1/(math.tan(sqrt(c_0*(1-x))))-sqrt(1/x-1)

    print('write precision (k) and max number of iterations (n)')
    k = float(input())
    n = int(input())
    a = 0.01
    b = 0.7
    if f(a) * f(b) < 0:
        for i in range(1, n):
            print(e)
            if k < e:
                if f((a + b) / 2) * f(b) < 0:
                    a = (a + b) / 2
                else:
                    b = (a + b) / 2
                print('current number of iterations =', n)
            else:
                break
    else:
        print('change range or function has not any roots')
    print('root =', (a + b) / 2)


root()
