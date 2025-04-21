# Eiercicio 5: Factorial de un número positivo
# Hacer un programa para calcular el factorial de un número positivo
numero = int(input("Ingrese un número positivo y se le sacara el factorial "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i

print("El factorial de " + str(numero) + " es: " + str(resultado))