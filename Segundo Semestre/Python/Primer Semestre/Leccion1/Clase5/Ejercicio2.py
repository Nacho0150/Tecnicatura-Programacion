# Ejercicio: Operador or
#
# La pregunta es si un padre puede asistir al juego de su hijo.
# Verificamos si tiene vacaciones
# Verificamos si tiene el día libre
# Usar estructura ‘if else’ con el operador or
# Imprimir

# print("Le haremos preguntas para ver si puede asistir al juego de su hijo")
# preg = input("Tiene vacaciones? ")
# preg1 = input("Tiene ese día libre? ")

# if (str.capitalize(preg) == "No" and str.capitalize(preg1) == "Si"):
#     print("Usted puede asistir al juego de su hijo")
# else:
#     print("Usted no puede asistir al juego de su hijo")

vacaciones = True
diaDescanso = True

if not (vacaciones or diaDescanso):
    print("Usted no puede asistir al juego de su hijo")
else:
    print("Usted puede asistir al juego de su hijo")