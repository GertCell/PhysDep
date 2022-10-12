import numpy as np
from matplotlib.pyplot import *
X = []
Y = []

n = 10

for i in range(0, n):
    x = - 5 + i * 10 / n
    y = 1 / (1 + x ** 2)
    X.append(x)
    Y.append(y)

A = np.copy(Y)
m = len(X)

for j in range(1, n):

        for i in range(n-1, j-1, -1):
            A[i] = float(A[i]-A[i-1])/float(X[i]-X[i-j])

def p(x):
    P = A[0]
    t = (x - X[0])
    for j in range(1, n):
        P = P + t*A[j]
        t = t * (x - X[j])
    return P


fig, ax = subplots(1)
for i in range(0, m):
    ax.scatter(X[i], p(X[i]))
    gcf().canvas.draw()


