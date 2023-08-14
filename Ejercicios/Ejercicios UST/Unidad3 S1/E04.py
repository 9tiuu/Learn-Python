# - 9tiuu | Ejercicio 4 -
def contar_letras():

    palabra = 'abracadabra'
    midiccionario = {}

    for letras in palabra:
        d = {letras: palabra.count(letras)}
        midiccionario.update(d)

    print(f'({palabra}) -> {midiccionario}')

contar_letras()