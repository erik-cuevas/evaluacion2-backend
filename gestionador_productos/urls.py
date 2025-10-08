"""URLs de la app gestionador_productos.

Define rutas simples y nombres para uso con {% url %} en plantillas.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos/', views.listado_productos, name='listado'),
    path('productos/crear/', views.crear_producto, name='crear'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar'),
]
