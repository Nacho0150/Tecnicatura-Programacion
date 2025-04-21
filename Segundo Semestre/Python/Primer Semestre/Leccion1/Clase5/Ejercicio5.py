# Ejercicio: Tienda de libros
# Mostrar: Ingrese los siguientes datos del libro
# Digite el nombre del libro
# Digite el ID del libro
# Digite el precio del libro
# Indicar si el envío es gratuito (True/False)
# Mostrar:
# Nombre:
# ID:
# Precio:
# Envío Gratuito?:

print("Ingrese los siguientes datos del libro ")
nombre = input("Digite el nombre del libro: ")
id = input("Digite el ID del libro: ")
precio = float(input("Digite el precio del libro: "))
envio = bool(input("Indicar si el envío es gratuito (True/False): "))

print(f"\nNombre: {nombre}\n"
      f"ID: {id}\n"
      f"Precio: {precio}\n"
      f"Envío Gratuito?: {envio}")