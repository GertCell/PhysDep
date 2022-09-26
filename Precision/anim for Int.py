from numpy import *
from matplotlib.pyplot import *
# This code works only in jupyter notebook
# %matplotlib notebook


def f(x):
    return 1 / (x ** 2 + 1)


S1 = []
S2 = []
I = []
v = np.pi / 2

# Parameters

a = 1
b = -1

# Segment splitting

n = 100
d = (b - a) / n

subplot(111)
ln, = plot(I, S2)
ln1, = plot(I, S1)
axis([0, 100, -1, 1])

xi = a
xi_1 = xi + d
xi_2 = xi_1 + d
s1 = d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
for i in range(0, n - 1):
    xi = xi_1
    xi_1 = xi + d
    xi_2 = xi_1 + d
    s = s1
    s1 = s + d / 3 * (f(xi) + 4 * f(xi_1) + f(xi_2))
    S2.append(v + s1 / 2)
    I.append(i)

xi = a
xi_1 = xi + d
s1 = (f(xi_1) + f(xi)) * d
for i in range(0, n - 1):
    xi = xi_1
    xi_1 = xi + d
    s = s1
    s1 = s + (f(xi_1) + f(xi)) * d
    S1.append(v + s1 / 2)

ln.set_data(I, S2)
ln1.set_data(I, S1)
gcf().canvas.draw()

