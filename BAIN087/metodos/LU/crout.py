from fractions import Fraction
import numpy as np

def crout(A):
    n = len(A)
    L = np.zeros((n, n), dtype=object)
    U = np.zeros((n, n), dtype=object)

    for i in range(n):
        # Calcular elementos de la matriz U
        for k in range(i, n):
            sum_upper = sum(L[i, j] * U[j, k] for j in range(i))
            U[i, k] = A[i][k] - sum_upper

        # Calcular elementos de la matriz L
        for k in range(i, n):
            if i == k:
                L[i, i] = Fraction(1, 1)
            else:
                sum_lower = sum(L[k, j] * U[j, i] for j in range(i))
                L[k, i] = Fraction(A[k][i] - sum_lower, U[i, i])

    return L, U

