# - 9tiuu | Ejercicio 17 -

def cantidadpares(numero):
    pares = 0

    for n in range(numero, -1, -1):
        if n % 2 == 0:
            pares += 1
    return pares

num = int(input("Numero: "))
npares = cantidadpares(num)

print(f"Entre el {num} y el {0} hay {npares} numeros pares")
