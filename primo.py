"""Función final, después del ciclo TDD Red-Green-Refactor."""


def es_primo(numero: int) -> bool:
    """Indica si un entero mayor o igual a 2 es primo."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True
