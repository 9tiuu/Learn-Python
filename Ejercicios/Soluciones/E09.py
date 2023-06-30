# - 9tiuu | Ejercicio 9 -

def palabras(a, b):
    if a == b:
        return True
    elif a != b:
        return False

p1 = input("Ingrese una palabra: ")
p2 = input("Ingrese otra palabra: ")
resultado = palabras(p1, p2)

print(resultado)
