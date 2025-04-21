# Diseñar un programa que ingresando un año, nos devuelva
# por consola si es un año biciesto o no, repetir la accion
# hasta que el usuario lo desida

op = 1
print("Comprobamos que año es biciesto")

while op == 1:
    anio = int(input("Ingrese el año\n"))

    if (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} es biciesto")
    else:
        print(f"El año {anio} no es biciesto")

    op = int(input("Si desea continuar, ingrese 1, de lo contrario ingrese 2\n"))