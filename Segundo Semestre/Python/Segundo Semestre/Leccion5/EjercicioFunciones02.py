# Ejercicio 2: Función con * args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentol
def sumValores(*args):
    result = 1

    for valor in args:
        result *= valor
    return result

print(sumValores(3, 5, 9, 2, 1))