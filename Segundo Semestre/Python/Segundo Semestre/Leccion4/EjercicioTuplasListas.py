import math # Importamos la clase math para hacer uso de la función sqrt(raíz cuadrada)
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los números menores a 5
# e imprimir por consola [1, 3, 2]

lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

# Ejercicio de matemáticas
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un número positivo '))
while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')