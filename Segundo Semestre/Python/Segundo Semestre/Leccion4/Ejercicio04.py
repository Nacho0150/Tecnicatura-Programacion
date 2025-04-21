# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#                          suma de números pares del 2 al 30
#                          suma = 240
print('Digite dos números y se sumaran los números pares dentro de ese rango')
numero = int(input('Número menor del rango '))
numero1 = int(input('Número mayor del rango '))
suma = 0

for i in range(numero, numero1 + 1):
    if i % 2 == 0:
        suma += i

print("La suma de los números pares en el rango (" + str(numero) + " - " + str(numero1) + ") es: " + str(suma))