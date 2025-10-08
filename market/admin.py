from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "precio", "created_at")
	search_fields = ("nombre", "descripcion")
	list_filter = ("created_at",)

# Producto registrado para administración
