#Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, Luego
# meter los caracteres en una lista sin repetir caracteres
cadena = input('Ingrese una cadena:\n')
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)

print(f'\nLista de caracteres sin repetir ninguno: \n {lista}')