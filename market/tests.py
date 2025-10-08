"""Shim de tests para compatibilidad: reexporta los tests desde la nueva app.

Esto evita fallos en entornos donde la suite intenta importar tests desde
`market.tests`.
"""

# Importar todo desde gestionador_productos.tests para que unittest descubra
# las mismas clases de test que antes.
from gestionador_productos.tests import *  # noqa: F401,F811
