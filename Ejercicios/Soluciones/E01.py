# - 9tiuu | Ejercicio 1 -

def masacorporal(peso, altura):

    imc = peso / (altura**2)

    if imc <= 15:
        print(f"IMC: {round(imc, 1)}, Delgadez muy severa.")
    elif imc > 15 and imc <= 15.9:
        print(f"IMC: {round(imc, 1)}, Delgadez severa.")
    elif imc >= 16  and imc <= 18.4:
        print(f"IMC: {round(imc, 1)}, Delgadez.")
    elif imc >= 18.5 and imc <= 24.9:
        print(f"IMC: {round(imc, 1)}, Peso saludable.")
    elif imc >= 25 and imc <= 29.9:
        print(f"IMC: {round(imc, 1)}, Sobrepeso.")
    elif imc >= 30 and imc <= 34.9:
        print(f"IMC: {round(imc, 1)}, Obesidad moderada.")
    elif imc >= 35 and imc <= 39.9:
        print(f"IMC: {round(imc, 1)}, Obesidad severa.")
    elif imc >= 40:
        print(f"IMC: {round(imc, 1)}, Obesidad muy severa.")

p = float(input("Ingrese su peso: "))
a = float(input("Ingrese su altura: "))

masacorporal(p, a) 
