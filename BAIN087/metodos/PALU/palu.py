"""
import numpy as np
from fractions import Fraction

def palu(matriz_A):
    n = len(matriz_A)
    
    # Inicializar matrices P, L y U
    P = np.eye(n, dtype=Fraction)
    L = np.eye(n, dtype=Fraction)
    U = np.array(matriz_A, dtype=Fraction)
    
    for k in range(n - 1):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(U[k:, k])) + k
        if max_index != k:
            # Intercambiar filas en U
            U[[k, max_index], :] = U[[max_index, k], :]
            # Intercambiar filas en P y L
            P[[k, max_index], :] = P[[max_index, k], :]
            L[[k, max_index], :k] = L[[max_index, k], :k]
        
        # Eliminación gaussiana
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    
    return P, L, U

"""
import numpy as np
from fractions import Fraction

def palu(matriz_A):
    n = len(matriz_A)
    
    # Inicializar matrices P, L y U
    P = np.eye(n, dtype=Fraction)
    L = np.eye(n, dtype=Fraction)
    U = np.array(matriz_A, dtype=Fraction)
    
    for k in range(n - 1):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(U[k:, k])) + k
        if max_index != k:
            # Intercambiar filas en U
            U[[k, max_index], :] = U[[max_index, k], :]
            # Intercambiar filas en P y L
            P[[k, max_index], :] = P[[max_index, k], :]
            L[[k, max_index], :k] = L[[max_index, k], :k]
        
        # Eliminación gaussiana
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    
    return P, L, U
