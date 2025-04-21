class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        print('Estamos utilizando el método get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método Setter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property
    def apellido(self):  # Método Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método Setter
        self._apellido = apellido

    @property
    def edad(self):  # Método Getter
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # Llamamos al método getter
    persona1.nombre = 'Juan Pedro'  # Llamamos al método setter
    print(persona1.nombre)  # Otra vez con el método getter
    print(persona1.mostrar_detalles())  # Llamamos al método mostrar_detalles
    # Atributo read-only (sólo lectura) sería la edad porque no tiene el método set
    print(persona1.edad)

    # Tarea crear tres objetos más, utilizando los métodos getter and setter
    # para modificar, y mostrar los cambios con el método mostrar detalles

    # Objeto número 1 de la tarea
    persona2 = Persona2('Flor', 'Romer', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Florencia'
    persona2.apellido = 'Romery'
    persona2.edad = 22
    print(persona2.mostrar_detalles())

    # Objeto número 2 de la tarea
    persona3 = Persona2('Nacho', 'Garcia', 22)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3._nombre = 'Ignacio'
    persona3.apellido = 'Ibañez'
    persona3.edad = 23
    print(persona3.mostrar_detalles())

    # Objeto número 3 de la tarea
    persona4 = Persona2('Marcos', 'Garcia', 29)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Marco'
    persona4.apellido = 'Ibañez'
    persona4.edad = 19
    print(persona4.mostrar_detalles())

    print(__name__)
