# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 Lista de palabras que aparecen en ambas Listas

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lista1 = [9, 8, 7, 6, 5, 5, 6, 7 , 8, 9]

# Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto = set(lista)
conjunto1 = set(lista1)

link = list(conjunto | conjunto1)
firstList = list(conjunto - conjunto1)
secList = list(conjunto1 - conjunto)
intersection = list(conjunto & conjunto1)

print(f"Lista de palabras que aparecen en las listas: {link}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {firstList}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {secList}")
print(f"Lista de palabras que aparecen en ambas listas: {intersection}")