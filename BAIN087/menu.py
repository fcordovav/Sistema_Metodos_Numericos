import os
def mostrarMenu():
    with open("db/menu.txt", "r", encoding = "utf-8") as archivo:
        lineas = archivo.readlines()
                            
        for linea in lineas:
            print(f"\t{linea.strip()}")

def limpiarConsola():
    sistema_operativo = os.name
    if sistema_operativo == "posix": #linux y mac
        os.system("clear")
    elif sistema_operativo == "nt": #windows
        os.system("cls")