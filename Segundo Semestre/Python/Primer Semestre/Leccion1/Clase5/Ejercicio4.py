# Ejercicio: El mayor de dos números
# Solicitar al usuario dos valores, determinar cual es el mayor.
# Solicitar al usuario dos valores
# numero1 (int)
# numero2 (int)
# Se debe imprimir el mayor de los dos números (La salida debe ser identica a la siguiente):
# Digite el valor para el numero1:
# Digite el valor para el numero2:
# El número mayor es:   <numeroMayor>

print("Ingrese dos valores y verificaremos cual es el mayor")
numero1 = int(input("Digite el valor para el numero1: "))
numero2 = int(input("Digite el valor para el numero2: "))

if (numero1 > numero2):
    print(f"El valor número1: {numero1}, es mayor que el número2: {numero2}")
else:
    print(f"El valor número2: {numero2}, es mayor que el número1: {numero1}")