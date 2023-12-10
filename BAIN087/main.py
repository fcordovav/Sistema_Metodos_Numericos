import menu
import eleccionOperacion

def main():
    print("\n¡Bienvenido al sistema de Métodos Numéricos BAIN087!")
    print("Antes de comenzar debes modificar su matriz A y b!\n")

    matriz_A = [
        [4,3,-1,1],
        [1,-2,2,-3],
        [2,-3,2,-1],
        [1,1,-3,-2]
    ]
    matriz_b = [5,5,5,5]
    
    while True:
        menu.mostrarMenu()
        eleccion = int(input("\nEscoja su operación: "))
        if eleccion == 0:
            break
        eleccionOperacion.operacion(matriz_A, matriz_b, eleccion)

    print("\nPrograma terminado!\n")

if __name__ == "__main__":
    main()

