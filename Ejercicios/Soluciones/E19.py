# - 9tiuu | Ejercicio 19 -

numero = int(input("Ingrese un numero: "))

if numero < 2:
    print("No se puede dibujar un cuadrado")
else:
    for altura in range(numero):
        print(numero * str(numero))
        numero -= 1
  