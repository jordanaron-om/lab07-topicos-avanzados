"""Versión inicial: decisiones y cálculos mezclados en una sola función."""
import math


def calcular_area(tipo, valor1, valor2=0):
    if tipo == "rectangulo":
        return valor1 * valor2
    elif tipo == "circulo":
        return math.pi * valor1 * valor1
    elif tipo == "triangulo":
        return valor1 * valor2 / 2
    else:
        raise ValueError("Figura no reconocida")


if __name__ == "__main__":
    print("=== AREAS: VERSION INICIAL ===")
    print(f"Rectangulo: {calcular_area('rectangulo', 4, 6):.2f}")
    print(f"Circulo: {calcular_area('circulo', 3):.2f}")
    print(f"Triangulo: {calcular_area('triangulo', 5, 8):.2f}")
