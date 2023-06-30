# - 9tiuu | Ejercicio 20 -

rep = 10
pares = []
impares = []

while rep:
    numero = int(input("Ingrese un numero: "))
    rep -= 1
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print(f"""
Lista de numeros pares: {pares}
Lista de numeros impares: {impares}
""")
