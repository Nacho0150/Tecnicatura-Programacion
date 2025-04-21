class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con
    un método calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input('Ingrese el ancho del cubo \n'))
altura = int(input('Ingrese la altura del cubo \n'))
profundidad = int(input('Ingrese la profundidad del cubo \n'))

cub = Cubo(ancho, altura, profundidad)

print(f'El volumén de su cubo es: {cub.calcular_volumen()}')