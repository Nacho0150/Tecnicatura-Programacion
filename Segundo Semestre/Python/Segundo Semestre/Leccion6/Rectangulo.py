class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tenér 2 atributos: altura y base
    el nombre del método será calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcularArea(self):
        return self.base * self.altura

base = int(input('Ingrese la base del rectángulo \n'))
altura = int(input('Ingrese la altura del rectángulo \n'))

rect = Rectangulo(altura, base)

print(f'El area de su rectángulo es: {rect.calcularArea()}')