"""Demuestra SRP y OCP con rectángulo y círculo."""
from figuras_base import Rectangulo, Circulo
from presentacion_areas import mostrar_areas


if __name__ == "__main__":
    print("=== SOLID: FIGURAS ORIGINALES ===")
    mostrar_areas([
        ("Rectangulo", Rectangulo(4, 6)),
        ("Circulo", Circulo(3)),
    ])
