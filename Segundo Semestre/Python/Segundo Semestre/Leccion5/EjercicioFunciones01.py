# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# numéricos, utilizando argumentos variables *args como parametro de la
# Función y agregar como resultado la suma de todos los valores pasados
# como argumentos.
def sumValores(*args):
    result = 0

    for valor in args:
        result += valor
    return result

print(sumValores(3, 5, 9, 2, 1))