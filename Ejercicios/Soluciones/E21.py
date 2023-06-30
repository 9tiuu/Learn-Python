# - 9tiuu | Ejercicio 21 -

lista = ['Adiós', 'asignatura', 'introducción', 'a', 'la', 'programación']

# a) insertar palabra en indice 1:
palabra = input('Insertar palabra: ')
lista.insert(1, palabra)

# b) Mostrar indice de la palabra "introducción" sin saber el tamaño de la lista:
print(f'El indice de "introducción" es:', lista.index('introducción'))

# c) Modificar el ultimo elemento de la lista sin saber el tamaño de la lista:
palabra2 = input('Modificar palabra: ')
for indice in range(len(lista)):
    x = indice
del lista[x] # o simplemente: del lista[-1] = palabra2
lista.append(palabra2)

# d) imprimir lista (resultado completo):
print(lista)
