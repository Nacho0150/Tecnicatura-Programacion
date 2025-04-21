# Ejercicio: Rango entre las edades 20 y 30 años
#
# Preguntar la edad al usuario
# Si la edad esta dentro de los 20 o 30 años, esta dentro del rango
# Combinamos los operadores and y or para saber si el usuario esta dentro del rango o no

edad = int(input("Ingrese su edad "))
veinte = edad >= 20 and edad < 30
treinta = edad >= 30 and edad < 40

if (veinte or treinta):
    print("Estás dentro del rango de los 20 o 30 años")
else:
    print("No estás dentro del rango de los 20 o 30 años")