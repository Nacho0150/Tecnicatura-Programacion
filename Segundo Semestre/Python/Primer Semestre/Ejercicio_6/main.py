# Ejercicio 6: Ingresar "N" enteros, visualizar la suma de los
# números pares de la lista, cuántos números pares
# existen y cuál es el promedio de los números
# impares.

n = int(input("Ingrese la cantidad de números que desea ingresar\n"))

sumaNPar = 0
cantPar = 0
sumaNImpar = 0
cantImpar = 0

for i in range(n):
    a = int(input("Ingrese un número\n"))

    if a % 2 == 0:
        sumaNPar += a
        cantPar += 1
    else:
        sumaNImpar += a
        cantImpar += 1

if sumaNImpar == 0 and cantImpar == 0:
    promImpar = 0
else:
    promImpar = sumaNImpar / cantImpar

print(f"La suma de los números pares es: {sumaNPar}")
print(f"La cantidad de números pares ingresados es de: {cantPar}")
print(f"El promedio de los números impares es de: {promImpar}")