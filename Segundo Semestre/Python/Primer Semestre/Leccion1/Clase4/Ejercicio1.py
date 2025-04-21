# Instrucciones de la tarea Clase4: Ejercicio Rectángulo
# En el siguiente ejercicio se solicita calcular el área y el perímetro de un rectángulo. Para ello debemos de crear las siguientes variables:
# alto (int)
# ancho (int)

alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
print("")

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")