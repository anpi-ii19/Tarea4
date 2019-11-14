import numpy as np
import matplotlib.pyplot as plt
from edo2 import edo2


# Calculo de la solucion exacta del problema
x = np.arange(1, 6, 0.001)
y = np.sin(6 - x) / (np.sin(5) * np.sqrt(x))

p = '-1 / x'
q = '(1 / (4 * x ** 2)) - 1'
f = '0'

# Calculo utilizando el metodo edo2 y un h = 10 ** -1
h_1 = 10 ** -1
x_1, y_1 = edo2(p, q, f, h_1, 1, 6, 1, 0)
label = 'h=10**-' + str(1)

# Calculo utilizando el metodo edo2 y un h = 10 ** -2
h_2 = 10 ** -2
x_2, y_2 = edo2(p, q, f, h_2, 1, 6, 1, 0)
label = 'h=10**-' + str(1)

# Calculo utilizando el metodo edo2 y un h = 10 ** -3
h_3 = 10 ** -3
x_3, y_3 = edo2(p, q, f, h_3, 1, 6, 1, 0)
label = 'h=10**-' + str(1)

# Graficacion de los resultados obtenidos
label = 'exacta'
plt.plot(x, y, label=label)
plt.legend()
plt.pause(2)

label_1 = 'h = ' + str(h_1)
plt.plot(x_1, y_1, label=label_1)
plt.legend()
plt.pause(2)

label_2 = 'h = ' + str(h_2)
plt.plot(x_2, y_2, label=label_2)
plt.legend()
plt.pause(2)

label_3 = 'h = ' + str(h_3)
plt.plot(x_3, y_3, label=label_3)
plt.legend()
plt.pause(2)
