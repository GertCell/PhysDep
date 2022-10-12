from matplotlib.pyplot import *
import numpy as np

N = 100

H = 1
T = 1

a = 0.5
h = a * H / N
t = T / N

d = a * h / t

X = np.arange(0, H, h)
U = [3] * len(X)
U[0] = 5
UU = []

fig, ax = subplots(1)
axis([0, 1, 0, 5])
ax.set_title('Wave')
ax.set_xlabel('Distance')
ax.set_ylabel('Wave Speed')

for time in np.arange(0, T, t):
    UU = U

    for i in range(0, N + 1):
        U[i] = UU[i] + d*(UU[i - 1] - UU[i])

    ax.plot(X, U)
    fig.canvas.show()
    cla()

    y = 1
    U[y] = 5
    y += 1



