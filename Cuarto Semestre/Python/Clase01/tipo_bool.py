
# Bool contiene los valores True y False
# Los tipos numéricos, es false para el 0 (cero), true para los cemás valores
valor = 0
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor: {valor}, Resultado: {resultado}')

# Tipo String -> False '', True demás valores
valor = ''
resultado = bool(valor)
print(f'valor: "{valor}", Resultado: {resultado}')

valor = 'Hola'
resultado = bool(valor)
print(f'valor: "{valor}", Resultado: {resultado}')

# Tipo colecciones -> False par colecciones vacias
# Tipo colecciones -> True par todas las demás
# Lista
valor = []
resultado = bool(valor)
print(f'valor de una lista vacia: {valor}, Resultado: {resultado}')

valor = [1, 2, 3]
resultado = bool(valor)
print(f'valor de una lista con elementos: {valor}, Resultado: {resultado}')

# Tuplas
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, Resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor de una tupla con elementos: {valor}, Resultado: {resultado}')

# Diccionarios
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool
if (1,):
    print('Regresa verdadero')
else:
    print('Regresa falso')

# Ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')