# BY 9tiuu

import os
os.system('cls')

print("""
|=== Calcular promedio ===|
| (1) Promedio del ramo   |
| (2) Promedio semestre   |
""")

try:
    asd01 = int(input('Opcion: ').strip())
    print()

    if asd01 == 1:

        print('Ingresar NOTA como decimal y con PUNTO, ejemplo: 7.0 \nIngresar POCENTAJE como decimal y con PUNTO, ejemplo: 15% -> 0.15')
        print()

        nota1 = float(input('Nota 1: ').strip())
        porcentaje1 = float(input('Porcentaje: ').strip())
        print()

        nota2 = float(input('Nota 2: ').strip())
        porcentaje2 = float(input('Porcentaje: ').strip())
        print()

        nota3 = float(input('Nota 3: ').strip())
        porcentaje3 = float(input('Porcentaje: ').strip())
        print()

        nota4 = float(input('Nota 4: ').strip())
        porcentaje4 = float(input('Porcentaje: ').strip())
        print()

        promedio = (nota1 * porcentaje1) + (nota2 * porcentaje2) + (nota3 * porcentaje3) + (nota4 * porcentaje4)
        print(f'Promedio de asignatura: {round(promedio, 2)}')
        print()

    elif asd01 == 2:

        ramos = int(input('Total de asignaturas: ').strip())
        print()

        cantidad_de_ramos = ramos
        contador = 1

        notas = []

        while ramos:
            nota = float(input(f'Promedio de asignatura {contador}: ').strip())
            notas.append(nota)
            contador += 1
            ramos -= 1
        print()
        
        suma_de_notas = 0

        for n in notas:
            suma_de_notas += n

        promedio_final = suma_de_notas / cantidad_de_ramos
        print(f'Promedio final: {round(promedio_final, 2)}')
        print()

    else:
        print('NOTA: No hay mas opciones... \nVuelve a ejecutar el programa...')
        print()
except:
    print()
    print('NOTA: Escriba alguna de las 2 opciones... \nVuelve a ejecutar el programa...')
    print()