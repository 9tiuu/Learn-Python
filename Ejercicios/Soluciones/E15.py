# - 9tiuu | Ejercicio 15 -

palabra = input("Palabra: ")

for letra in palabra:
    if letra == "o" or letra == "O":
        letra = "x"
    print(letra, end="")