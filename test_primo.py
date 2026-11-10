"""Pruebas escritas antes de implementar por completo es_primo."""
import pytest
from primo import es_primo


@pytest.mark.parametrize(
    "numero, esperado",
    [
        (-1, False), (0, False), (1, False),
        (2, True), (3, True), (4, False),
        (9, False), (17, True), (21, False), (29, True),
    ],
)
def test_es_primo(numero, esperado):
    assert es_primo(numero) is esperado
