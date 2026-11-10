"""Extensión OCP: nueva figura sin cambiar Figura, Circulo o Rectangulo."""
from figuras_base import Figura


class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura / 2
