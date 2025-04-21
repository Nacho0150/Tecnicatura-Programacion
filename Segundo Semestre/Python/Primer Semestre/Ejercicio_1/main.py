# Calcular la suma de "N" primeros números

n = int(input("Ingrese la cantidad de números a sumarse\n"))
suma = 0

for i in range(0,n):
    a = int(input("Ingrese el número a sumar\n"))
    suma += a

print(f"La suma de {n} números es igual a {suma}")