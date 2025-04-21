# Eiercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada
def recursivo(numero):
    if numero >= 1:
        print(numero)
        recursivo(numero - 1)
    elif numero <= 0:
        print('Número ingresado incorrecto')

num = int(input('Ingrese un número y se le mostrara descendentemente\n'))
recursivo(num)