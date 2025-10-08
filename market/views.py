from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm


def inicio(request):
    return render(request, "paginas/inicio.html")


def nosotros(request):
    return render(request, "paginas/nosotros.html")


def listado_productos(request):
    """Lista todos los productos desde la base de datos."""
    productos = Producto.objects.all().order_by('-created_at')
    return render(request, "listado.html", {"productos": productos})


def crear_producto(request):
    """Crea un producto usando POST. Protegido con CSRF en template."""
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listado")
    else:
        form = ProductoForm()
    return render(request, "crear.html", {"form": form})


def eliminar_producto(request, pk):
    """Elimina el producto identificado por pk; solo POST para confirmar la acción."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("listado")
    return render(request, "eliminar.html", {"producto": producto})
