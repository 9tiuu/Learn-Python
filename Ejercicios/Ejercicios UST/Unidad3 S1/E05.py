# - 9tiuu | Ejercicio 5 -
def es_subcadena():

    cadena = 'Hola mundo'
    subcadena = 'mundo'

    palabras = cadena.split()

    if subcadena in palabras:
        print(f'({cadena}, {subcadena}) -> {True}')
    else:
        print(f'({cadena}, {subcadena}) -> {False}')

es_subcadena()