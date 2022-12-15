import numpy as np
import matplotlib.pyplot as plt


N = 1000
A_0 = 0.5
X_0 = 0.5
x = np.linspace(0, 1, N)
A = lambda x: A_0 + (1 - A_0)*(1- x/X_0)**2
a = A(x)
plt.title('Форма сопла')
plt.plot(x, a)
plt.xlabel('x')
plt.ylabel('A(x)')
