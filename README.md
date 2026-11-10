# Laboratorio 7 - Tópicos avanzados y calidad de código

Proyecto académico del curso Lenguajes de Programación.

## Actividades
- Control de versiones con Git y GitHub.
- Refactorización de cálculo de áreas.
- TDD de la función `es_primo` con pytest.
- SOLID: SRP y Open/Closed mediante figuras geométricas.

## Ejecución
Se recomienda abrir esta carpeta en Visual Studio Code.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q test_primo.py
```

Los archivos en `etapas_tdd/` representan tres momentos de una práctica TDD; se copian temporalmente a `primo.py` siguiendo la guía de capturas.
Esta rama incorpora una mejora a la documentación del proyecto.