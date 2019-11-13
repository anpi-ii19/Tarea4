from sympy import lambdify
import numpy as np
from thomas import thomas


def edo2(p, q, f, h, a, b, y0, yn):
    """
    Metodo de Diferencias Divididas que da solucion a la ecuacion
    y'' = p(x)y'(x) + q(x)y(x) + f(x) en un intervalo [a, b]
    :param p: String con la funcion que multiplica al y'(t) en la ecuacion,
              debe estar en termino de "x"
    :param q: String con la funcion que multiplica al y(t) en la ecuacion,
              debe estar en termino de "x"
    :param f: String con la funcion f(x) mostrada en la ecuacion,
              debe estar en termino de "x"
    :param h: Numero positivo, corresponde al tamaño de paso
    :param a: Numero que corresponde al extremo inferior del intervalo [a, b]
    :param b: Numero que corresponde al extremo superior del intervalo [a, b]
    :param y0: Numero que corresponde al valor inicial en x = a
    :param yn: Numero que corresponde al valor inicial en x = b
    :return: Vector columna "x" y vector columna "y" que dan solucion al sistema,
             ambos son Numpy Matrix
    """
    if h < 0:
        return "El tamaño de paso h debe ser un numero positivo"

    if a > b:
        return "Los extremos de los intervalor son incorrectos"

    p = lambdify('x', p)
    q = lambdify('x', q)
    f = lambdify('x', f)

    t = a
    soporte = []
    # Se construye el conjunto soporte
    while t <= b - h:
        soporte.append(t)
        t += h

    n = len(soporte)
    matriz_A = np.matrix(np.zeros((n, n)))
    matriz_b = np.matrix(np.zeros((n, 1)))

    # Se construye la matriz tridiagonal matriz_A y el vector columna b
    for i in range(0, n):
        si = soporte[i]
        pi = p(si)
        qi = q(si)
        fi = f(si)

        # Construccion de la matriz matriz_A
        # Se inserta el elemento bi
        bi = 2 + (h ** 2) * qi
        matriz_A[i, i] = bi

        # Se inserta el elemento ai
        if i != 0:  # En la primer fila no existe un ai
            ai = (-h / 2) * pi - 1
            matriz_A[i, i - 1] = ai

        # Se inserta el elemento ci
        if i != n - 1:  # En la ultima fila no existe un ci
            ci = (h / 2) * pi - 1
            matriz_A[i, i + 1] = ci

        # Construccion del vector columna b
        di = -h ** 2 * fi
        # Caso especial i = 0
        if i == 0:
            # Se inserta el primer elemento
            e0 = ((h / 2) * pi + 1) * y0
            matriz_b[i, 0] = di + e0

        # Caso especial i = n - 1
        if i == n - 1:
            en = ((-h / 2) * pi + 1) * yn
            matriz_b[i, 0] = di + en

        # Si no es ningun caso especial
        if i != 0 and i != n - 1:
            matriz_b[i, 0] = di

    # Con las matrices A y b, se procede a encontrar la solucion del sistema A y = b
    y = thomas(matriz_A, matriz_b)

    return soporte, y
