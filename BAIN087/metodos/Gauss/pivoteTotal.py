
import numpy as np
from fractions import Fraction

def gauss_total(matriz_A, matriz_b):
    matriz_A = np.array(matriz_A, dtype=float)
    matriz_b = np.array(matriz_b, dtype=float)
    sistema_ecuaciones = np.column_stack((matriz_A, matriz_b))

    n = len(matriz_b)
    indices_columnas_originales = np.arange(n)

    for i in range(n):
        max_value = 0.0
        max_row = i
        max_col = i
        for row in range(i, n):
            for col in range(i, n):
                if abs(sistema_ecuaciones[row, col]) > max_value:
                    max_value = abs(sistema_ecuaciones[row, col])
                    max_row = row
                    max_col = col

        # Intercambiar filas
        sistema_ecuaciones[[i, max_row]] = sistema_ecuaciones[[max_row, i]]
        
        # Intercambiar columnas solo en la matriz A
        sistema_ecuaciones[:, :n][:, [i, max_col]] = sistema_ecuaciones[:, :n][:, [max_col, i]]

        # También actualizar los índices originales de las columnas
        indices_columnas_originales[[i, max_col]] = indices_columnas_originales[[max_col, i]]

        # Eliminación hacia adelante
        sistema_ecuaciones[i, :] /= sistema_ecuaciones[i, i]
        for j in range(i + 1, n):
            sistema_ecuaciones[j, :] -= sistema_ecuaciones[j, i] * sistema_ecuaciones[i, :]

    soluciones = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soluciones[i] = sistema_ecuaciones[i, -1]
        soluciones[i] -= np.dot(sistema_ecuaciones[i, i+1:n], soluciones[i+1:])

    indices_ordenados = np.argsort(indices_columnas_originales)
    soluciones_ordenadas = soluciones[indices_ordenados]

    soluciones_finales = [Fraction(sol).limit_denominator() for sol in soluciones_ordenadas]
    return soluciones_finales



"""
import numpy as np
from fractions import Fraction

def gauss_total(matriz_A, matriz_b):
    matriz_A = np.array(matriz_A, dtype=float)
    matriz_b = np.array(matriz_b, dtype=float)
    sistema_ecuaciones = np.column_stack((matriz_A, matriz_b))

    n = len(matriz_b)
    pivotes = {}

    for i in range(n):
        # Pivoteo total: encontrar el elemento con el mayor valor absoluto en la submatriz A restante
        max_index_A = np.unravel_index(np.argmax(np.abs(matriz_A[i:, i:])), matriz_A[i:, i:].shape)
        max_index_A = (max_index_A[0] + i, max_index_A[1] + i)

        # Intercambiar filas de la matriz A
        matriz_A[[i, max_index_A[0]], :] = matriz_A[[max_index_A[0], i], :]
        # Intercambiar filas de la matriz ampliada
        sistema_ecuaciones[[i, max_index_A[0]], :] = sistema_ecuaciones[[max_index_A[0], i], :]

        # Intercambiar columnas de la matriz A
        matriz_A[:, [i, max_index_A[1]]] = matriz_A[:, [max_index_A[1], i]]
        # Intercambiar columnas de la matriz ampliada
        sistema_ecuaciones[:, [i, max_index_A[1]]] = sistema_ecuaciones[:, [max_index_A[1], i]]

        if matriz_A[i, i] == 0:
            print(f"El pivote en la fila {i + 1} y columna {i + 1} es cero. La eliminación de Gauss no es posible.")
            return None, None, None, None

        for j in range(i + 1, n):
            multiplicador = matriz_A[j, i] / matriz_A[i, i]
            pivote_key = f"m{j+1}{i+1}"
            pivotes[pivote_key] = multiplicador

            matriz_A[j, :] -= multiplicador * matriz_A[i, :]
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
    matriz_A_resultante = np.zeros_like(matriz_A, dtype=object)
    for i in range(n):
        for j in range(n):
            matriz_A_resultante[i, j] = Fraction(matriz_A[i, j]).limit_denominator()

    # Guardar la matriz b resultante como fracciones
    matriz_b_resultante = np.zeros_like(matriz_b, dtype=object)
    for i in range(n):
        matriz_b_resultante[i] = Fraction(sistema_ecuaciones[i, -1]).limit_denominator()

    return soluciones, pivotes, matriz_A_resultante, matriz_b_resultante


"""


