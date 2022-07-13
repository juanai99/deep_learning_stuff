

import matplotlib.pyplot as plt
import numpy as np

f = lambda x : x**4 - 2*x**2 + x
f_grad = lambda x : 4*x**3 - 4*x + 1

def a():
    x = np.arange(-3, 3, 0.1)
    y = f(x)
    plt.plot(x, y, 'b-')

def b():
    y = f(2)
    y_ = f_grad(2)
    print([y, y_])

def c():
    eta = 0.05
    n = 30
    x = 2

    x_list = list()
    x_list.append(x)
    y_list = list()
    y_list.append(f(x)+1)

    for _ in range(n):
        x = x - eta * f_grad(x)
        x_list.append(x)
        y_list.append(f(x)+1)

    plt.plot(x_list, y_list, 'r.')

def d():
    eta = 0.02
    rho = 0.8
    n = 30
    x = 2

    x_list = list()
    x_list.append(x)
    y_list = list()
    y_list.append(f(x)+1)

    v = 0
    for _ in range(n):
        v = rho*v - f_grad(x)
        x = x + eta * v
        x_list.append(x)
        y_list.append(f(x)+1)

    plt.plot(x_list, y_list, 'r.')

a()
d()
plt.show()
