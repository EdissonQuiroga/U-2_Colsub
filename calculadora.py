"""Calculadora suma y resta"""

def suma (num1,num2):
    return num1+num2

def resta (num1,num2):
    return num1-num2

def calculadora():
    print("1 Suma")
    print("2 Resta")
    print("3 Opcion Equivocada")
    opcion = input("--> ")
    return opcion

num1 = float(input("Introduzca Numero:  "))

while True:
    op = calculadora()

    num2= float(input("Introduzca Numero:  "))

    if op == "1":
        resultado = suma(num1,num2)
    elif op == "2":
        resultado = resta(num1,num2)

    print("El Resultado es: ", resultado)

    continuar = input("Continue realizando operaciones (s/n):  ")
    if continuar == "n":
        break