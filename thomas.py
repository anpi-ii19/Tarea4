import numpy as np


def thomas(A, b):
    """
    Algoritmo de Thomas para resolver un sistema A x = b para matrices tridiagonales
    :param A: Numpy Matrix, donde A es una matriz tridiagonal invertible de tamaño n x n
    :param b: Numpy Matrix, donde b es un vector columna de tamaño n
    :return: Numpy Matrix, donde x es un vector columna de tamaño n que resuelve el sistema Ax=b
    """
    A = np.matrix(A)
    b = np.matrix(b)

    # Se verifican las dimensiones de A y b
    n, m = A.shape
    if n != m:
        return "La matriz A debe ser cuadrada"

    if n != b.shape[0]:
        return "A debe tener la misma cantidad de filas que b"

    x = []
    p = []
    q = []

    # Calculo del vector p y q

    # Caso especial i = 0
    p0 = A.item(0, 1) / A.item(0, 0)
    q0 = b.item(0, 0) / A.item(0, 0)
    p.append(p0)
    q.append(q0)

    # Calculo de los pi y qi desde i = 1 hasta i = n - 1
    for i in range(1, n):
        ai = A.item(i, i - 1)  # Se obtiene el ai
        bi = A.item(i, i)  # Se obtiene el bi
        di = b.item(i, 0)  # Se obtiene el di

        qi = (di - q[i - 1] * ai) / (bi - p[i - 1] * ai)  # Se obtiene el qi
        q.append(qi)

        # Las iteraciones en el vector p llegan hasta i = n - 1, por lo que
        # es necesario evitar que se realice el calculo en este valor de i
        if i != n - 1:
            ci = A.item(i, i + 1)  # Se obtiene el ci
            pi = ci / (bi - p[i - 1] * ai)  # Se calcula el pi
            p.append(pi)

    # Calculo del vector x

    # Caso especial i = n
    x.append([q.pop()])

    # Calculo de los xi restantes
    for i in range(2, n + 1):
        # Se recoren las listas p y q en orden descendente
        q_i = q.pop()
        p_i = p.pop()
        x_i1 = x[-i + 1][0]
        xi = q_i - p_i * x_i1
        x.insert(0, [xi])

    return np.matrix(x)
