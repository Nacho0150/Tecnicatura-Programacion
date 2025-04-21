from math import pi
# Ejercicio 4
# Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia
radio = float(input("Ingrese el radio del circulo: "))
area = pi * radio ** 2
longitud = 2 * pi * radio
print(f"Los resultados de la expresion son: area:{area} longitud:{longitud}")