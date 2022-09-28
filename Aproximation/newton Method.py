
import numpy as np
import matplotlib.pyplot as plt

n = 7  # 5, 6 ... 15 Number of points
X = []
Y = []
a = []
# Points
for i in range(1, n+1):
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

    B = a[0] + a[1] * X[1]**2
    B1 = B + a[i-1]*X[i-1]**2

    a[i] = (Y[i] - B1)/X[i]**2
    i += 1
print(a)
