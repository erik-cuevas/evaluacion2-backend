"""Formularios para crear/editar Producto.

Usamos ModelForm para mapear automáticamente campos del modelo.
"""

from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """Formulario basado en `Producto`.

    Define widgets para obtener campos con estilo Bootstrap.
    """

    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "imagen"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    # Notas:
    # - Este ModelForm mapea directamente los campos del modelo Producto.
    # - Para validaciones personalizadas (por ejemplo validar dimensiones de
    #   la imagen) extender el método clean_imagen o clean() del formulario.
