# 1 Task

import matplotlib.pyplot as plt

# Constants

a = 0.5
# time tick

T = 1
H = 1
N = 500

t = T/(N-1)
h = a*H/(N-1)
X = [0]*N

for i in range(0, N):
    X[i] = i*h


def wave():

    # Arrays

    U = [3] * N
    U[0] = 5
    time = 0

    fig, ax = plt.subplots(1, 1)

    while time < T:
        time = time + t

        # {запоминаем поле температуры на предыдущем слое по времени}


        UU = U

        for j in range(0, N):
            U[j] = UU[j] + a*t/h*(UU[j-1]-UU[j])

        plt.axis([0, 1, 2.5, 5])

        plt.plot(X, U)
        fig.canvas.draw()
        plt.show()
    return 0


wave()