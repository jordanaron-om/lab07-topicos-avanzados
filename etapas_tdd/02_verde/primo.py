"""Etapa VERDE: solución mínima correcta, todavía mejorable."""


def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True
