# BY 9tiuu | Update code: 24/12/23
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
        print('\nIngresar NOTA como decimal y con PUNTO, ejemplo: 7.0')
        print('Ingresar POCENTAJE como decimal y con PUNTO, ejemplo: 15% -> 0.15')

        nota1 = float(input('\nNota 1: ').strip())
        porcentaje1 = float(input('Porcentaje: ').strip())

        nota2 = float(input('\nNota 2: ').strip())
        porcentaje2 = float(input('Porcentaje: ').strip())

        nota3 = float(input('\nNota 3: ').strip())
        porcentaje3 = float(input('Porcentaje: ').strip())

        nota4 = float(input('\nNota 4: ').strip())
        porcentaje4 = float(input('Porcentaje: ').strip())

        promedio = (nota1 * porcentaje1) + (nota2 * porcentaje2) + (nota3 * porcentaje3) + (nota4 * porcentaje4)
        print(f'\nPromedio de asignatura: {round(promedio, 2)}\n')

    elif asd01 == 2:
        ramos = int(input('Total de asignaturas: ').strip())
        cantidad_de_ramos = ramos
        contador = 1
        notas = []

        while ramos:
            nota = float(input(f'\nPromedio de asignatura {contador}: ').strip())
            notas.append(nota)
            contador += 1
            ramos -= 1
        
        suma_de_notas = 0

        for n in notas:
            suma_de_notas += n

        promedio_final = suma_de_notas / cantidad_de_ramos
        print(f'\nPromedio final: {round(promedio_final, 2)}\n')

    else:
        print('\n> NOTA: No hay mas opciones... \nVuelve a ejecutar el programa...\n')
        
except:
    print('\n> NOTA: Escriba alguna de las 2 opciones... \nVuelve a ejecutar el programa...\n')
