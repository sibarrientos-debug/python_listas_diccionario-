def agregar_videojuegos(videojuegos):
    print("\n ---Agrear Video Juego---")

    try:
        id_juego=int(input("Ingrese ID del video juego"))
    except ValueError:
        print("El ID debe ser númerico. ")
        return
    

    nombre = input("Ingrese nombre del videojuego: ").strip()
    genero = input("Ingrese género del videojuego: ").strip()

    if nombre == "" or genero == "":
       print("El nombre y el género no pueden quedar vacíos.")
       return
    
    try:
        precio = int(input("Ingrese precio del videojuego: "))
    except ValueError:
        print("El precio debe ser numérico.")
        return
    
    if precio <= 0:
        print("El precio debe ser mayor a cero.")
        return
    
    videojuego = {
                "id": id_juego,
                "nombre": nombre,
                "genero": genero,
                "precio": precio
                }
    videojuegos.append(videojuego)
    print("Videojuego agregado correctamente.")