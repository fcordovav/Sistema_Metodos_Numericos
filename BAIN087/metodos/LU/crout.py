from fractions import Fraction
import numpy as np

def crout(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.eye(n)

    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p] * U[p][k]
        L[k][k] = A[k][k] - suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p] * U[p][k]
            L[i][k] = (A[i][k]-suma2) / (U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p] * U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
    return L,U
