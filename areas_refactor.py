"""Versión refactorizada: nombres específicos y funciones pequeñas."""
import math


def area_rectangulo(base, altura):
    return base * altura


def area_circulo(radio):
    return math.pi * radio ** 2


def area_triangulo(base, altura):
    return base * altura / 2


def mostrar_areas():
    print("=== AREAS: VERSION REFACTORIZADA ===")
    print(f"Rectangulo: {area_rectangulo(4, 6):.2f}")
    print(f"Circulo: {area_circulo(3):.2f}")
    print(f"Triangulo: {area_triangulo(5, 8):.2f}")


if __name__ == "__main__":
    mostrar_areas()
