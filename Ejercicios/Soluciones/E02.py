# - 9tiuu | Ejercicio 2 -

p = input("Palabra: ")
total = 0

for a in p:
    if a == "a":
        total += 1
print(f'La palabra "{p}" contiene {total} caracteres "a"')
