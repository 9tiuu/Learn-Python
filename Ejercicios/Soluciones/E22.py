# - 9tiuu | Ejercicio 22 -

frutas = {'platano': 1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}

fruit = input('Fruta: ')

if fruit in frutas:    
    kilos = int(input('Cantidad (K): '))
    
    if kilos == 0:
        print(f'{fruit}: {frutas[fruit]}')
    else:
        print(f'{fruit}: {frutas[fruit] * kilos}')

else:
    print(f'"{fruit}" No se ha encontrado')
