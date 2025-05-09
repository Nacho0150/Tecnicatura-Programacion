from NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurió un error: {type(e)}')
else:
    print("No se arrojo ninguna excepión")
finally: # Siempre se va a ejecutar
    print("Ejecución de este bloque finally")

print(f'El resultado es: {resultado}')
print('seguimos...')