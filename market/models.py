from django.db import models


# Modelo principal para la evaluación: Producto
# Campos: nombre (titulo), descripcion, precio (campo extra relevante)
class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(blank=True)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:  # para mostrar en admin y listas
		return f"{self.nombre} - ${self.precio}"
