from metodos.Gauss.pivoteNormal import gauss
from metodos.Gauss.pivoteParcial import gauss_parcial
from metodos.Gauss.pivoteTotal import gauss_total
from metodos.LU.doolittle import doolittle
from metodos.LU.crout import crout
from metodos.PALU.palu import palu
import menu
import prints


def main():
    print("\n¡Bienvenido al sistema de Métodos Numéricos BAIN087!")
    print("Antes de comenzar debes modificar su matriz A y b!\n")

    """
    matriz_A = [
        [2, -1, 1],
        [-3, -1, 4],
        [-1, 2, 3],
    ]

    matriz_b = [8, 1, 4]
    """

    matriz_A = [
        [25,15,-5,-10],
        [15,10,1,-7],
        [-5,1,21,4],
        [-10,-7,4,18]
    ]
    """
    matriz_A = [
        [4,2,1],
        [10,3,8],
        [8,12,10],
    ]
    """
    matriz_b = [5,5,5,5]


    menu.mostrarMenu()
    eleccion = int(input("\nEscoja su operación: "))

    if eleccion in [1, 2, 3]:
        if eleccion == 1:
            soluciones, pivotes, matriz_A_resultante, matriz_b_resultante = gauss(matriz_A, matriz_b)
        elif eleccion == 2:
            soluciones, pivotes, matriz_A_resultante, matriz_b_resultante = gauss_parcial(matriz_A, matriz_b)
        else:
            #soluciones, pivotes, matriz_A_resultante, matriz_b_resultante = gauss_total(matriz_A, matriz_b)
            #soluciones = gauss_total(matriz_A, matriz_b)
            #for i, sol in enumerate(soluciones):
            #   print(f"\tx{i + 1} = {sol}")
            print("Esta opción aun no esta implementada!")
            return None

        prints.printMatriz(matriz_A_resultante, "A")
        prints.printB(matriz_b_resultante)
        prints.printSoluciones(soluciones)
        prints.printPivotes(pivotes)

    if eleccion in [4, 5]:
        if eleccion == 4:
            L, U = doolittle(matriz_A)
        else:
            print("Esta opcion tiene errores\n")
            return None
            L, U = crout(matriz_A)
        prints.printMatriz(L, "L")
        prints.printMatriz(U, "U")
    
    if eleccion == 6:
        P, L, U = palu(matriz_A)
        prints.printMatriz(P, "P")
        prints.printMatriz(L, "L")
        prints.printMatriz(U, "U")


    print("\nPrograma terminado!")


if __name__ == "__main__":
    main()

