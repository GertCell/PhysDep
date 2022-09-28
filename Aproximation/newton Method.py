
import numpy as np
import matplotlib.pyplot as plt

n = 4  # 5, 6 ... 15 Number of points
X = []
Y = []

# Points
for i in range(1, n+1):
    xi = -5 + i * 10 / n
    yi = 1 / (1 + xi ** 2)
    X.append(xi)
    Y.append(yi)

print(X, Y)

# Ordinary polynom

# P(x) = a0 + a1 (x1 - x0) +

