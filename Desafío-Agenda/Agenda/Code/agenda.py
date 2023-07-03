# ACUMULATIVA 3

agenda = [
    # Contactos integrados por defecto:
    {'nombre':'Jeremy', 'numero':11112222},
    {'nombre':'Brayan', 'numero':33334444}]

import os

os.system("cls")
while True:
    print("""
    | == Menu de opciones == |
    | (1) Agregar contacto   |
    | (2) Modificar contacto |
    | (3) Eliminar contacto  |
    | (4) Ver contactos      |
    | (0) Salir              |
    |------------------------|
    | BY: Jeremy.C, Brayan.S | 
    """)

    try:
        respuesta = int(input("Ingrese una opcion: ").strip())
    except:
        print("> DATO INVALIDO")
        print()

    # ----------------------------------------- #
    os.system("cls")
    if respuesta == 1:
        print("== Agregar contacto ==")
        print()
        
        nombre = input("Nombre: ").strip().capitalize()

        try:
            maxcaracteres = 0
            numero = int(input("Numero (MAX 8 digitos): "))
            print()

            for n in str(numero):
                maxcaracteres += 1
            
            if maxcaracteres > 8:
                print("> EL MAXIMO DE CARACTERES ES DE 8 DIGITOS")
                print()
            else:
                nuevo_contacto = {'nombre':nombre, 'numero':numero}
                agenda.append(nuevo_contacto)
                print("> CONTACTO AGREGADO")  
                print()      
        except:
            print()
            print("> DATO INVALIDO")
            print()
        
        input("ENTER para volver al menu...")
        os.system("cls") 

    # ----------------------------------------- #
    elif respuesta == 2:
        print("== Modificar contacto ==")
        print()

        for buscar in agenda:
            print(f"- Nombre: {buscar['nombre']}")
        print()

        contacto_select = input("Nombre del contacto a modificar: ").strip().capitalize()
        print()
    
        for x in agenda:

            if contacto_select == x['nombre']:
                modificar_contacto = input("Nuevo NOMBRE: ").strip().capitalize()
                try:
                    maxdigitos = 0
                    modificar_numero = int(input("Nuevo NUMERO (MAX 8 digitos): ").strip())
                    print()

                    for p in str(modificar_numero):
                        maxdigitos += 1
            
                    if maxdigitos > 8:
                        print("> EL MAXIMO DE CARACTERES ES DE 8 DIGITOS")
                        print()
                    else:
                        print("> CONTACTO MODIFICADO")
                        print()

                        x['nombre'] = modificar_contacto
                        x['numero'] = modificar_numero
                except:
                    print("> DATO INVALIDO")
                    print()

        input("ENTER para volver al menu...")
        os.system("cls") 

    # ----------------------------------------- #
    elif respuesta == 3:
        print("== Eliminar contacto ==")
        print()

        for contacs in agenda:
            print(f"- Nombre: {contacs['nombre']}")
        print()

        nombre_contacto = input("Nombre del contacto a eliminar: ").strip().capitalize()
        print()

        for c in agenda:
            if nombre_contacto == c['nombre']:
                agenda.remove(c)
                print("> CONTACTO ELIMINADO")
                print()
        
        input("ENTER para volver al menu...")
        os.system("cls") 

    # ----------------------------------------- #
    elif respuesta == 4:
        print("== Contactos ==")
        print()
        
        for contact in agenda:
            print(f"Nombre: {contact['nombre']}")
            print(f"Numero: {contact['numero']}")
            print("---------------")
        print()

        input("ENTER para volver al menu...")
        os.system("cls")  
    # ----------------------------------------- #
    elif respuesta == 0:
        print()       
        input("ENTER para salir...")
        print()
        break
    else:
        print()
        print("> OPCION INVALIDA, intentelo nuevamente")