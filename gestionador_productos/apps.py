"""Configuración de la aplicación gestionador_productos.

Este archivo registra el nombre del paquete para Django.
"""

from django.apps import AppConfig


class GestionadorProductosConfig(AppConfig):
    """Configuración de la app gestionador_productos.

    name debe coincidir con el paquete (gestionador_productos).
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestionador_productos'
