import numpy as np
from fractions import Fraction

def gauss_parcial(matriz_A, matriz_b):
    matriz_A = np.array(matriz_A, dtype=float)
    matriz_b = np.array(matriz_b, dtype=float)
    sistema_ecuaciones = np.column_stack((matriz_A, matriz_b))

    n = len(matriz_b)
    pivotes = {}

    for i in range(n):
        # Pivoteo parcial: encontrar la fila con el mayor valor absoluto en la columna actual
        max_index = np.argmax(np.abs(sistema_ecuaciones[i:, i])) + i
        # Intercambiar filas
        sistema_ecuaciones[[i, max_index], :] = sistema_ecuaciones[[max_index, i], :]

        for j in range(i + 1, n):
            multiplicador = sistema_ecuaciones[j, i] / sistema_ecuaciones[i, i]
            pivote_key = f"m{j+1}{i+1}"
            pivotes[pivote_key] = multiplicador

            sistema_ecuaciones[j, :] -= multiplicador * sistema_ecuaciones[i, :]

    soluciones = np.zeros(n, dtype=object)
    for i in range(n - 1, -1, -1):
        soluciones[i] = Fraction(sistema_ecuaciones[i, -1])
        for j in range(i + 1, n):
            soluciones[i] -= sistema_ecuaciones[i, j] * soluciones[j]

        soluciones[i] /= sistema_ecuaciones[i, i]

    # Convertir las soluciones a fracciones
    soluciones = [Fraction(sol).limit_denominator() for sol in soluciones]

    # Guardar la matriz A resultante como fracciones
    matriz_A_resultante = np.zeros_like(sistema_ecuaciones[:, :-1], dtype=object)
    for i in range(n):
        for j in range(n):
            matriz_A_resultante[i, j] = Fraction(sistema_ecuaciones[i, j]).limit_denominator()

    # Guardar la matriz b resultante como fracciones
    matriz_b_resultante = np.zeros_like(matriz_b, dtype=object)
    for i in range(n):
        matriz_b_resultante[i] = Fraction(sistema_ecuaciones[i, -1]).limit_denominator()

    return soluciones, pivotes, matriz_A_resultante, matriz_b_resultante


