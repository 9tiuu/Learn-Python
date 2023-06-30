# - 9tiuu | Ejercicio 7 -

def numeros(n1, n2):
    if n1 == n2:
        print("Ambos numeros son iguales")
    elif n1 > n2:
        print(f"{n1} Es el mayor")
    else:
        print(f"{n2} Es el mayor")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
numeros(num1, num2)