"""Responsabilidad independiente: mostrar resultados de figuras."""
from figuras_base import Figura


def mostrar_areas(figuras: list[tuple[str, Figura]]) -> None:
    for nombre, figura in figuras:
        print(f"{nombre}: {figura.area():.2f}")
