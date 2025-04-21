# Ejercicio: Valor dentro de un rango
#
# Pedimos al usuario un valor numérico
# Verificar si el valor ingresado se encuentra entre el rango de 0 a 5
# La formula es: <num> >= 0  and  <num> <= 5

num = int(input("Ingrese un valor numérico "))

if (num >= 0 and num <= 5):
    print(f"El valor {num} esta en el rango de 0 a 5")
else:
    print(f"El valor {num} no esta en el rango de 0 a 5")