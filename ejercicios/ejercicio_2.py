#Cree una clase Punto que represente un punto en el plano cartesiano#

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx ** 2 + dy ** 2) ** 0.5


punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

print(f"Punto 1: {punto1}")
print(f"Punto 2: {punto2}")
print(f"Distancia entre los puntos: {punto1.distancia(punto2)}")
