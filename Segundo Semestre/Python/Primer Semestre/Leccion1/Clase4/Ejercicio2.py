# Ejercicio Clase4: Número par o impar
#
# Solicitamos que el usuario ingrese un número
# Este se asigna a una variable
# Utilizaremos la estructura ‘if else’
# La formula: <num> % 2 == 0 Esta operación nos dice si es un número par
# Si es True imprimimos que es par
# Si es False imprimimos que es impar
# A hacer el ejercicio en PyCharm

num = int(input("Ingrese un número y le diremos si es par o impar "))

if (num % 2 == 0):
    print(f"El número: {num} es par")
else:
    print(f"El número: {num} es impar")