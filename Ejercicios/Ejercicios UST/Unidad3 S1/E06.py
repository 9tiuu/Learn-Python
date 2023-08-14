# - 9tiuu | Ejercicio 6 -
def ordenar_lista():

    lista_original = [3, 1, 4, 1, 5, 9, 2, 6]
    nueva_lista = []

    for numeros in lista_original:
        nueva_lista.append(numeros)
        nueva_lista.sort()

    print(f'({lista_original}) -> {nueva_lista}')

ordenar_lista()