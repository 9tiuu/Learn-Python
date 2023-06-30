# - 9tiuu | Ejercicio 16 -

def precio(dolares):
    clp = 793.58 # cambia su valor cierto tiempo
    pesos = dolares * clp
    print(f"{dolares} dolar/es son: {round(pesos, 2)} pesos chilenos")

d = int(input("Dolar/es: "))
precio(d)