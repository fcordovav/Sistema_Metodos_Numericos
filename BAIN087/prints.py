from fractions import Fraction

def printMatriz(matriz, nombre):
    print(f"\nMatriz {nombre} resultante:")
    for fila in matriz:
        for elem in fila:
            frac_elem = Fraction(elem).limit_denominator()
            print(f"\t{frac_elem}", end="")
        print()
    print()

def printB(matriz):
    print("\nMatriz b resultante:")
    for elem in matriz:
        print(f"\t{elem}")

def printSoluciones(soluciones):
    print("\nSoluciones:")
    for i, sol in enumerate(soluciones):
        print(f"\tx{i + 1} = {sol}")
    print()

def printPivotes(pivotes):
    print("\nMultiplicadores:")
    for key, value in pivotes.items():
        print(f"\t{key} = {Fraction(value).limit_denominator()}")
    print()