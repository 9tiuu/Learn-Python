# - 9tiuu | Ejercicio 8 -

def totalvocales(palabra):
    vocales = 0
    
    for letra in palabra:
        if letra == "a" or letra == "e":
            vocales += 1
        elif letra == "i" or letra == "o" or letra == "u":
            vocales += 1
    print(f'La palabra "{palabra}" contiene {vocales} vocales')

p = input("Palabra: ")
totalvocales(p)
