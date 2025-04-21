# Ejercicio 5: Sistema de Calificaciones

nota = int(input("Ingrese un valor del 0 al 10 y le diremos su calificación "))

if (nota == 9 or nota == 10):
    print("Su calificación es: A")
elif (nota >= 8 and nota < 9):
    print("Su calificación es: B")
elif (nota >= 7 and nota < 8):
    print("Su calificación es: C")
elif (nota >= 6 and nota < 7):
    print("Su calificación es: D")
elif (nota >= 0 and nota < 6):
    print("Su calificación es: F")
else:
    print("El valor ingresado es incorrecto")