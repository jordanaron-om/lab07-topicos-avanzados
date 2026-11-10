"""El reporte funciona también con una nueva clase Triangulo."""
from figuras_base import Rectangulo, Circulo
from figuras_extension import Triangulo
from presentacion_areas import mostrar_areas


if __name__ == "__main__":
    print("=== SOLID: NUEVA FIGURA SIN CAMBIAR EL MODULO BASE ===")
    mostrar_areas([
        ("Rectangulo", Rectangulo(4, 6)),
        ("Circulo", Circulo(3)),
        ("Triangulo", Triangulo(5, 8)),
    ])
