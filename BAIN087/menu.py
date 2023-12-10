def mostrarMenu():
    with open("db/menu.txt", "r", encoding = "utf-8") as archivo:
        lineas = archivo.readlines()
                            
        for linea in lineas:
            print(f"\t{linea.strip()}")