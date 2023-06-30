# - 9tiuu | Ejercicio 18 -

def nuevapalabra(palabra):
    frase = ""
    
    for letra in palabra:
        if letra == "b" or letra == "B":
            frase += "8"
        elif letra == "s" or letra == "S":
            frase += "$"
        elif letra == "g" or letra == "G":
            frase += "6"
        elif letra == "frase" or letra == "L":
            frase += "7"
        elif letra == "u" or letra == "U":
            frase += "x"
        else:
            frase += letra
    return frase

p = input("Palabra: ")
resultado = nuevapalabra(p)
print(resultado)
