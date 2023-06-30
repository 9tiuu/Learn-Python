# - 9tiuu | Ejercicio 11 -

def fecha(dia, mes, año):
    # Año bisiesto
    if año % 4 == 0 and mes == 2 and dia > 0 and dia < 30: 
        return True
    elif año % 4 != 0 and mes == 2 and dia > 0 and dia < 29: 
        return True
    # Fecha correcta
    elif mes % 2 != 0 and mes < 13 and dia > 0 and dia <= 31:
        return True
    elif mes != 2 and mes % 2 == 0 and mes > 0 and dia > 0 and dia <= 30:
        return True
    else:
        return False
    
d = int(input("Dia: "))
m = int(input("Mes: "))
a = int(input("Año: "))

fechacorrecta = fecha(d, m, a)
print(fechacorrecta)