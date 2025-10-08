"""Registro de modelos en el admin de Django para la app gestionador_productos."""

from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuración de la interfaz admin para el modelo Producto."""
    list_display = ("nombre", "precio", "created_at")
    search_fields = ("nombre", "descripcion")
    list_filter = ("created_at",)

# Fin de admin
