# - 9tiuu | Ejercicio 10 -

def numprimo(num):
    for numero in range(2, num):
        if num % numero == 0:
            return "El numero no es primo"
    return "El numero es primo"

n = int(input("Ingrese un numero: "))
resultado = numprimo(n)

print(resultado)