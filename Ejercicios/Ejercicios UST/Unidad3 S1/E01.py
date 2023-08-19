# - 9tiuu | Ejercicio 1 -
def interaccion_listas():

    lista0 = []
    lista1 = [1, 2, 3, 4]
    lista2 = [3, 4, 5, 6]

    for numero in lista1:
        if numero in lista2:
            lista0.append(numero)

    print(f'{lista1}, {lista2} -> {lista0}')

interaccion_listas()
