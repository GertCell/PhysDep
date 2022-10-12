import numpy as np
import matplotlib.pyplot as plt

n = 7  # 5, 6 ... 15 Number of points
X = []
Y = []
a = []
P = []
x = np.arange(0, 10, 0.1)
# Points
for i in range(1, n + 1):
    xi = -5 + i * 10 / n
    yi = 1 / (1 + xi ** 2)
    X.append(xi)
    Y.append(yi)
    a.append(0)


def f1(yi_1, yi_2, xi_1):
    return (yi_2 - yi_1)/(X[0]-xi_1)


a[0] = Y[0]
i = 1
a[i] = f1(Y[i], Y[i-1], X[i])


def delta_1(m):
    return (f1(Y[m], Y[m-1], X[m]) - f1(Y[m+1], Y[m], X[m+1]))/(X[0] - X[m])

i = 2
while i < n:
    i += 1
    a[i] = (delta_1(i+1) - delta_1(i))/(X[0]-X[i])
    i += 1
    a[i] = (delta_1(i+1) - delta_1(i))/(X[0]-X[i])
    




def p(x):
    P = a[0]
    t = (x - X[0])
    for j in range(1, n):
        P = P + t*a[j]
        t = t * (x - X[j])
        print(P)
    return 0


plt.plot(x, p(x))
plt.show()

