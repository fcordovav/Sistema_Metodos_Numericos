from metodos.Gauss.pivoteNormal import gauss
from metodos.Gauss.pivoteParcial import gauss_parcial
from metodos.Gauss.pivoteTotal import gauss_total
from metodos.LU.doolittle import doolittle
from metodos.LU.crout import crout
from metodos.PALU.palu import palu
import prints
import menu

def operacion(matriz_A, matriz_b, eleccion):
    try:
        if eleccion == 1:
            soluciones, pivotes, matriz_A_resultante, matriz_b_resultante = gauss(matriz_A, matriz_b)
        elif eleccion == 2:
            soluciones, pivotes, matriz_A_resultante, matriz_b_resultante = gauss_parcial(matriz_A, matriz_b)
        elif eleccion == 3:
            raise NotImplementedError("Esta opción aún no está implementada correctamente!")
        elif eleccion == 4:
            L, U = doolittle(matriz_A)
        elif eleccion == 5:
            L, U = crout(matriz_A)
        elif eleccion == 6:
            P, L, U = palu(matriz_A)
        elif eleccion == 7:
            menu.limpiarConsola()
        else:
            raise ValueError("Elección no válida")

    except (ValueError, NotImplementedError) as e:
        raise SystemExit(f"\nError: {e}\n")
    else:
        if eleccion in [1, 2, 3]:
            prints.printMatriz(matriz_A_resultante, "A")
            prints.printB(matriz_b_resultante)
            prints.printSoluciones(soluciones)
            prints.printPivotes(pivotes)
        elif eleccion in [4, 5]:
            prints.printMatriz(L, "L")
            prints.printMatriz(U, "U")
        elif eleccion == 6:
            prints.printMatriz(P, "P")
            prints.printMatriz(L, "L")
            prints.printMatriz(U, "U")
        

