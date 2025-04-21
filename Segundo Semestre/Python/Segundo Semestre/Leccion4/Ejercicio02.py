# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los número del 1 al 10, luego modificar los
# elementos de la lista multiplicandolos por un valor ingresado por el usuario

lista = []

for i in range(1, 11):
    lista.append(i)

num = int(input('\nDigite un número a multiplicar '))
for indice, i in enumerate(lista):
    lista[indice] *= num

print(lista)