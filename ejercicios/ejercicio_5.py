import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def pertenece(self, punto):
        distancia_centro_punto = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro_punto <= self.radio


# Ejemplo de uso
centro = Punto(0, 0)
circulo = Circulo(centro, 5)

punto1 = Punto(3, 4)
punto2 = Punto(6, 8)

print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")
print(f"¿Punto 1 pertenece al círculo?: {circulo.pertenece(punto1)}")
print(f"¿Punto 2 pertenece al círculo?: {circulo.pertenece(punto2)}")
