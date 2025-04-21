# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro programa dejaría de insertar.
# Por último, mostrar los números ordenados de menor a mayor

lista = []
while True:
    num = int(input('\nDigite números y se los ordenara de manera ascendente '))
    lista.append(num)
    if num == 0:
        break

lista.sort()
print(f'\nLista ordenada: \n{lista}')