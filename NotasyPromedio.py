"""Ingresar tres notas y sacar promedio"""

num1 = float(input("Ingrese Nota numero uno  "))
num2 = float(input("Ingrese Nota numero dos  "))
num3 = float(input("Ingrese Nota numero tres  "))

promedio = (num1+num2+num3)/3
print("El promedio de las notas es:  ", round(promedio,1))

n = promedio

if promedio>=8:
    print("Felicitaciones")
elif promedio<6:
    print("Deficiente")
if 6 <= n <= 7.9:
    print("Buen Trabajo")
