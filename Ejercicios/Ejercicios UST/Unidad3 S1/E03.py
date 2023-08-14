# - 9tiuu | Ejercicio 3 -
def obtener_elementos():

    letras = ('a', 'b', 'c', 'd')
    indices = [1, 3]
    nueva_tupla = ()

    nueva_tupla = list(nueva_tupla)

    for i in indices:
        nueva_tupla.append(letras[i])

    nueva_tupla = tuple(nueva_tupla)
    print(f'{letras}, {indices} -> {nueva_tupla}')
         
obtener_elementos()