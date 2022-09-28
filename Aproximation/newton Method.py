import numpy as np
import matplotlib.pyplot as plt

n = 7  # 5, 6 ... 15 Number of points
X = []
Y = []
a = []
P = []
# Points
for i in range(1, n + 1):
    xi = -5 + i * 10 / n
    yi = 1 / (1 + xi ** 2)
    X.append(xi)
    Y.append(yi)
    a.append(0)

print(Y[0])
# Ordinary polynom

a[0] = Y[0]
a[1] = (Y[1] - a[0]) / X[1]
i = 3
while i < n:
    B = a[0] + a[1] * X[1] ** 2
    B1 = B + a[i - 1] * X[i - 1] ** (i - 1)

    a[i] = (Y[i] - B1) / X[i] ** i
    i += 1
print(a)


def p(x):
    r = a[0]
    for j in range(1, n):
        t = a[j] * x ** i
        r = a[0] + t
    return r


for i in range(0, n+1):
    u = p(X[i])
    P.append(u)


plt.plot(X, Y)
plt.plot(X, P)

