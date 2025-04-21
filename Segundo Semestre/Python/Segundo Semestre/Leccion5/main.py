# Comenzamos con Funciones
# mi_Funcion() # No se puede llamar antes de definir a una función
# Definimos una función
def mi_Funcion(): # Para identificar a la función utilizamos paréntesis
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_Funcion() # Estamos llamando a la función
mi_Funcion() # Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)
person = ["Ignacio", "Ibañez"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la función
show(*person) # Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") # desempaquetamiento a través de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con la lista vacia se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se terminó")

# List comprehesion, lista de compresión
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"}]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a través del canal de YouTube")
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55, 45)}')

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas', 'José', 'Claudia', 'Rosaria', 'María')
listarNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos): # Lo mas utilizado es **kwards para recibir los arguntos
    for llave, valor in terminos.items(): # kwards significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar
listarTerminos(IDE = 'Integreted Development Environment', PK = 'Primary Key')
listarTerminos(Nombre='Leonel Messi')

def desplegarNombres(nombres): #
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objeto iterable
desplegarNombres((10, 11)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas
def factotial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factotial(numero - 1) # Caso Recursivo
numeroFactorial = int(input('Digite el número para calcular el factorial: '))
resultado = factotial(numeroFactorial) # Lo hacemos en código duro
print(f'El factorial del número {numeroFactorial} es: {resultado}') # Tarea que el usuario ingrese el número para calcular el factorial