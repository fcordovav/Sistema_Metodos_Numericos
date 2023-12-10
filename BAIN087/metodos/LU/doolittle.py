from fractions import Fraction
import numpy as np

def doolittle(A):
    n = len(A)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)

    for i in range(n):
        # Calcular elementos de la matriz U
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum

        # Calcular elementos de la matriz L
        for k in range(i, n):
            if i == k:
                L[i][i] = Fraction(1, 1)
            else:
                sum = 0
                for j in range(i):
                    sum += L[k][j] * U[j][i]
                L[k][i] = Fraction(A[k][i] - sum, U[i][i])

    return L, U

