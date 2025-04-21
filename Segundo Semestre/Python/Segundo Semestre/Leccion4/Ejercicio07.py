# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.
import random

num = random.randint(1, 100)
numero = 0

print('Tendrá que ingresar un número positivo del 1 al 100 para adivinar')
while numero != num:
    numero = int(input("Ingrese un número \n"))
    if numero > num:
        print('El número ingresado (' + str(numero) + ') es mayor\n')
    elif numero < num:
        print('El número ingresado (' + str(numero) + ') es menor\n')

print('\nAdivinaste! el número era ' + str(num))