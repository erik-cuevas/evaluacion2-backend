"""Modelos para la app gestionador_productos.

Contiene el modelo principal `Producto` con campos básicos y una imagen opcional.
"""

from django.db import models


class Producto(models.Model):
    """Modelo que representa un producto en el inventario.

    Campos:
    - nombre: título/clave del producto
    - descripcion: texto libre (opcional)
    - precio: valor numérico con 2 decimales
    - imagen: archivo opcional que se guarda en media/productos/
    - created_at: fecha de creación (auto)
    """

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Texto representativo del producto (útil en admin y en logs)."""
        return f"{self.nombre} - ${self.precio}"

    class Meta:
        # Use the default table name for this app (gestionador_productos_producto)
        # and let Django manage it. We created that table in
        # gestionador_productos/migrations/0001_initial.py so it's safe to enable
        # management now and remove the old 'market' dependency later.
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
