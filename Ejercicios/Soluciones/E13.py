# - 9tiuu | Ejercicio 13 -

numero = int(input("Ingrese un numero: "))

if numero < 2:
    print("No se puede dibujar un cuadrado")
else:
    for altura in range(numero):
        figura = str(numero) * numero
        print(figura)
        