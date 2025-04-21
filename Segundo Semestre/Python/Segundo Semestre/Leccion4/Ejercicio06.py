# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,25,30,35, 40, 45,50
numero = int(input("Ingrese un número positivo y se le multiplicará del 1 al 10: \n"))
resultado = 0
lista = []

for i in range(1, 11):
    resultado = numero * i
    lista.append(resultado)

print('La multiplicación de ' + str(numero) + ' por el rango del 1 al 10 es: ', end='') # end para que no haga un salto de linea
for i in lista:
    print(i, end=' ')