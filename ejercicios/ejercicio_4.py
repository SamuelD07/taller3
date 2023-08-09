class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def base(self):
        return abs(self.esquina_inf_der.x - self.esquina_sup_izq.x)

    def altura(self):
        return abs(self.esquina_inf_der.y - self.esquina_sup_izq.y)

    def perimetro(self):
        return 2 * (self.base() + self.altura())

    def area(self):
        return self.base() * self.altura()

    def es_cuadrado(self):
        return self.base() == self.altura()


punto1 = Punto(1, 4)
punto2 = Punto(5, 1)
rectangulo = Rectangulo(punto1, punto2)

print(f"Base: {rectangulo.base()}")
print(f"Altura: {rectangulo.altura()}")
print(f"Perímetro: {rectangulo.perimetro()}")
print(f"Área: {rectangulo.area()}")
print(f"Es un cuadrado: {rectangulo.es_cuadrado()}")
