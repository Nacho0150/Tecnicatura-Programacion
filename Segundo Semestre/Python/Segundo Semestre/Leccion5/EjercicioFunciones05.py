# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas
def convertCelsToFah(grados):
    return (grados * 9/5) + 32

def convertFahToCels(grados):
    return (grados - 32) * 5/9

print('1- Convertir de grados celsius a fahrenheit')
print('2- Convertir de grados fahrenheit a celsius')
opc = int(input('Elija una opción\n'))
if opc == 1:
    grados = float(input('Ingrese los grados celcius a calcular\n'))
    celcius = convertCelsToFah(grados)
    print(f'Sus grados fahrenheit a celsius es: {celcius}')
elif opc == 2:
    grados = float(input('Ingrese los grados fahrenheit a calcular\n'))
    fahrenheit = convertFahToCels(grados)
    print(f'Sus grados celsius a fahrenheit es: {fahrenheit}')