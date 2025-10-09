"""Registro de modelos en el admin de Django para la app gestionador_productos."""

from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuración de la interfaz admin para el modelo Producto."""
    list_display = ("nombre", "precio", "created_at")
    search_fields = ("nombre", "descripcion")
    list_filter = ("created_at",)

# Notas de admin:
# - La configuración anterior muestra columnas útiles y permite búsqueda
#   por nombre y descripción. Puedes personalizar list_display para añadir
#   miniaturas o acciones inline si lo deseas.
