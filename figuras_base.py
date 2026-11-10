"""SOLID: las figuras calculan su área; el reporte queda separado."""
from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calcula el área, sin imprimir información."""


class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2
