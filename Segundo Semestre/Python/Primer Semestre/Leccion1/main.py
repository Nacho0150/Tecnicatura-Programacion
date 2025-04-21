''' """ para comentar
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben asi, la variable x = x832, la variable y = x576, la variable z = x896
print(id(y))
print(id(z))


# Tipos int, float. String, Bool
# a = "Hola alumnos"
# a: str = "Hola alumnos" # str es como referencia nomas, para que se sepa que tiene que ser string
# a = 10.78
# a = True/ False # siempre tiene que ser con la primera letra en mayuscula
# print(type(a))

x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))


# Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black:"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))


# Tipos de Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


# Procesar la entrada del usuario
# Funcion input
resultado = input("Digite un numero: ") # regresa un dato tipo string, es como el scanner de Java
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: ")) # se los transfotma en int, porque el dato que ingresen viene como string y se necesita int para la suma
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
fin de comentario """ '''

"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print("Resultado de la suma:", suma)
print(f'El resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'El resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')

division = operandoA // operandoB #devuelve un numero entero
print(f'El resultado de la division (int) es: {division}')

modulo = operandoA % operandoB # en la calculadora seria el resultado de la division menos los numeros antes de la coma y despues se multiplica por el divisor, ej: 8/5= 1.6 - 1 = 0.6*5= 3
print(f'El resultado de la division o residuo (modulo) es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado del exponente es: {exponente}')
"""


"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignacion

miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)


# Operadores de Comparacion

d = 4
b = 2
# Comprobamos si son iguales
resultado = d == b
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador Mayor que
resultado = d > b
print(resultado)

# Operador Menor que
resultado = d < b
print(resultado)

# Operador Menor o Igual que
resultado = d <= b
print(resultado)

# Operador Mayor o Igual que
resultado = d >= b
print(resultado)
"""

"""
# Operadores Lógicos

a = True
b = True
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)
"""