# - 9tiuu | Ejercicio 7 -
def obtener_inversa():

    tupla_original = (1, 2, 3, 4, 5)
    nueva_tupla = ()

    nueva_tupla = list(nueva_tupla)

    for numeros in tupla_original:
        nueva_tupla.append(numeros)
        nueva_tupla.sort()
        nueva_tupla.reverse()
    
    nueva_tupla = tuple(nueva_tupla)
    print(f'({tupla_original}) -> {nueva_tupla}')

obtener_inversa() 