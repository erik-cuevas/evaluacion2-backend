"""Vistas (views) de la aplicación gestionador_productos.

Se usan vistas basadas en funciones (function-based views) sencillas para:
- inicio: página principal
- nosotros: página informativa
- listado_productos: listar productos desde la base de datos
- crear_producto: formulario POST para crear productos
- eliminar_producto: confirmar y eliminar (POST)
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm


def inicio(request):
    """Renderiza la página principal (sin lógica adicional)."""
    return render(request, "paginas/inicio.html")


def nosotros(request):
    """Renderiza la página 'Nosotros'."""
    return render(request, "paginas/nosotros.html")


def listado_productos(request):
    """Consulta la BD y devuelve la plantilla con el listado de productos.

    La variable `productos` pasada a la plantilla es un QuerySet ordenado por fecha.
    """
    productos = Producto.objects.all().order_by('-created_at')
    return render(request, "listado.html", {"productos": productos})


def crear_producto(request):
    """Gestiona la creación de un Producto.

    Si la petición es POST, valida el formulario y guarda el objeto (incluyendo la imagen).
    Si es GET, muestra el formulario vacío.
    """
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listado")
    else:
        form = ProductoForm()
    return render(request, "crear.html", {"form": form})


def eliminar_producto(request, pk):
    """Muestra confirmación y elimina el producto en POST.

    Se usa get_object_or_404 para devolver 404 si pk no existe.
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("listado")
    return render(request, "eliminar.html", {"producto": producto})
