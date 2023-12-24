# Formativa 3 | Update code: 24/12/23
import os

biblioteca = [ # Libro integrado por defecto
    {'titulo':'Juan salvador gaviota', 'codigo':1, 'año':1970}]

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
        print("\n> DATO INVALIDO\n")

    # --------------------------------------------------------- #

    os.system("cls")

    if respuesta == 1:
        print("== Agregar libro ==\n")

        titulo = input("Titulo: ").strip().capitalize()
        try:
            codigo = int(input("Codigo: ").strip())
            año = int(input("Año: ").strip())

            if codigo < 0 or año < 0:
                print("\n> DATOS INGRESADOS NO VALIDOS\n")
                
            else:
                libro = {'codigo': codigo, 'titulo':titulo, 'año':año}
                biblioteca.append(libro)
                print("\n> LIBRO AGREGADO\n")

        except:
            print("\n> DATO INVALIDO\n")
        
        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 2:
        print("== Modificar libro ==\n")

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------\n")

        try:
            respuesta2 = int(input("Ingrese el codigo a MODIFICAR: ").strip())
        except:
            print("\n> DATO INVALIDO\n")

        for x in biblioteca:
            if respuesta2 == x['codigo']:
                mtitulo = input("\nNuevo titulo: ").strip().capitalize()
                
                try:
                    maño = int(input("Nuevo año: ").strip())
                    x['titulo'] = mtitulo
                    x['año'] = maño
                    print("\n> LIBRO MODIFICADO\n")

                except:
                    print("\n> DATO INVALIDO\n")

        input("ENTER para volver al menu...")
        os.system("cls")            

    # --------------------------------------------------------- #

    elif respuesta == 3:
        print("== Eliminar libro ==\n")

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------\n")

        try:
            respuesta3 = int(input("Codigo del libro a ELIMINAR: ").strip())
            
            for x in biblioteca:
                if respuesta3 == x['codigo']:
                    biblioteca.remove(x)
                    print("\n> LIBRO ELIMINADO\n")

        except:
            print("\n> DATO INVALIDO\n")
        
        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 4:
        print("== Listar biblioteca ==\n")

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
            print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
            print("-------------------------\n")

        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 5:
        print("== Listar biblioteca por año ==\n")

        try:
            respuesta5 = int(input("Ingrese el AÑO del libro: ").strip())
        except:
            print("\n> DATO INVALIDO\n")

        if biblioteca == []:
            print("\033[;33mNO HAY LIBROS EN LA BIBLIOTECA\033[;37m")

        for libros in biblioteca:
            if respuesta5 == libros['año']:
                print(f"Titulo: \033[;32m{libros['titulo']}\033[;37m")
                print(f"Año: {libros['año']} | Codigo: {libros['codigo']}")
                print("-------------------------\n")

        input("ENTER para volver al menu...")
        os.system("cls")

    # --------------------------------------------------------- #

    elif respuesta == 0:
        print("\n> Adios...\n")
        break

    else:
        print("\n> OPCION INVALIDA, intentelo nuevamente")
        
