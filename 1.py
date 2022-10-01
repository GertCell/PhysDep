from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import *
# This code works only in jupyter notebook
% matplotlib
notebook


def f(x):
    return x * (1 - x)


a = 1
b = 0
v = 1 / 6  # np.pi/2
print(v)
S1 = []
S2 = []
I = []
g, m = quad(f, a, b)
print(g)
# Parameters


# Segment splitting

# subplot(111)
# ln, = plot(I, S2)
# ln1, = plot(I, S1)
# axis([0, 100, 0, 2])

fig, ax = subplots(2)

for n in range(4, 50, 2):
    d = (b - a) / n
    xi = b
    xi_1 = xi + d
    xi_2 = xi_1 + d
    s1 = d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
    for i in range(1, n):
        xi = xi_1
        xi_1 = xi + d
        xi_2 = xi_1 + d
        s = s1
        s1 = s + d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
        I.append(i)
        g, m = quad(f, a, xi_2)
        S1.append(g - s1 / 2)

    xi = b
    xi_1 = xi + d
    s2 = (f(xi_1) + f(xi)) * d
    for i in range(1, n):
        xi = xi_1
        xi_1 = xi + d
        s = s2
        s2 = s + (f(xi_1) + f(xi)) * d
        g, m = quad(f, a, xi)
        S2.append(-g + s2 / 2)
    ax[0].scatter(i, v + s1 / 2)
    ax[0].scatter(i, v + s2 / 2)
    ax[1].plot(I, S1)
    ax[1].plot(I, S2)
    # ln.set_data(I, S2)
    # ln1.set_data(I, S1)
    gcf().canvas.draw()

