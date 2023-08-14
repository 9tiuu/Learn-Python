# - 9tiuu | Ejercicio 2 -
def eliminar_duplicados():

    lista_original = [1, 2, 3, 2, 4, 1, 5]
    nueva_lista = []

    for numeros in lista_original:
        nueva_lista.append(numeros)

        if nueva_lista.count(numeros) > 1:
            nueva_lista.remove(numeros)
            nueva_lista.sort()

    print(f'{lista_original} -> {nueva_lista}')
    
eliminar_duplicados()