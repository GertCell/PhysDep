import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

# entering constants

N = 5
t_end = 1
L = 0.05
l = 18
po = 4500
c = 530
T0 = 550
Tl = 1500
Tr = 550

# summation steps

a = l / (po * c)
h = L / (N - 1)
tau = h ** 2 / (4 * a)

# Temp arrays
T = [0] * N
TT = [0] * N

# {определяем поле температуры в начальный момент времени}
for i in range(1, N - 1):
    T[i] = T0
# {определяем значения температуры на границе}
T[0] = Tl

T[N - 1] = Tr
print(tau, h)

time = 0
fig, ax = plt.subplots(1, 1)
while time <= t_end:
    # Не забудь ты поменял шаг по времени!
    time = time + tau
    # {запоминаем поле температуры на предыдущем слое по времени}
    for i in range(0, N):
        TT[i] = T[i]
    # {определяем неизвестное поле температуры по соотношениям (12)}
    for j in range(1, N - 1):
        T[j] = TT[j] + (a * tau / h ** 2) * (TT[j + 1] - 2 * TT[j] + TT[j - 1])


    plt.axis([0, 50, Tr, 1500])
    ax.set_title('Temperature Distribution')
    ax.set_xlabel('Width (mm)')
    ax.set_ylabel('Temperature (C)')
    plt.plot(T)
    fig.canvas.draw()

