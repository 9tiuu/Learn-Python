# Formativa 3

biblioteca = [
    # Libro integrado por defecto
    {'titulo':'Juan salvador gaviota', 'codigo':1, 'año':1970}]

import os

os.system("cls")

while True:
    print(""" 
|  === Menu de opciones ===  |         
| (1) Agregar libro          |
| (2) Modificar libro        |
| (3) Eliminar libro         |
| (4) Listar biblioteca      |
| (5) Listar biblio por años |    
| (0) Salir del menu         |
|----------------------------|
|     Created by: Jeremy     |
""")
    
    try:
        respuesta = int(input("Ingrese una opcion: ").strip())
    except:
        print()
        print("> DATO INVALIDO")
        print() 

    # --------------------------------------------------------- #

    os.system("cls")

    if respuesta == 1:
        print("== Agregar libro ==")
        print()

        titulo = input("Titulo: ").strip().capitalize()
        try:
            codigo = int(input("Codigo: ").strip())
            año = int(input("Año: ").strip())

            if codigo < 0 or año < 0:
                print()
                print("> DATOS INGRESADOS NO VALIDOS")
                print()
            else:
                libro = {'codigo': codigo, 'titulo':titulo, 'año':año}
                biblioteca.append(libro)

                print()
                print("> LIBRO AGREGADO")
                print()

        except:
            print()
            print("> DATO INVALIDO")
            print()
        
        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 2:
        print("== Modificar libro ==")
        print()

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------")
        print()

        try:
            respuesta2 = int(input("Ingrese el codigo a MODIFICAR: ").strip())
            print()
        except:
            print()
            print("> DATO INVALIDO")
            print()

        for x in biblioteca:
            if respuesta2 == x['codigo']:

                mtitulo = input("Nuevo titulo: ").strip().capitalize()
                
                try:
                    maño = int(input("Nuevo año: ").strip())
                    print()

                    x['titulo'] = mtitulo
                    x['año'] = maño

                    print("> LIBRO MODIFICADO")
                    print()

                except:
                    print()
                    print("> DATO INVALIDO")
                    print()

        input("ENTER para volver al menu...")
        os.system("cls")            

    # --------------------------------------------------------- #

    elif respuesta == 3:
        print("== Eliminar libro ==")
        print()

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------")
        print()

        try:
            respuesta3 = int(input("Codigo del libro a ELIMINAR: ").strip())
            print()

            for x in biblioteca:
                if respuesta3 == x['codigo']:
                    biblioteca.remove(x)

                    print("> LIBRO ELIMINADO")
                    print()

        except:
            print()
            print("> DATO INVALIDO")
            print()
        
        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 4:
        print("== Listar biblioteca ==")
        print()

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------")
        print()

        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 5:
        print("== Listar biblioteca por año ==")
        print()

        try:
            respuesta5 = int(input("Ingrese el AÑO del libro: ").strip())
            print()
        except:
            print()
            print("> DATO INVALIDO")
            print()

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            if respuesta5 == libros['año']:
                print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
                print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
                print("-------------------------")
        print()

        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 0:
        print()
        print("> Adios...")
        print()
        break

    else:
        print()
        print("> OPCION INVALIDA, intentelo nuevamente")
        