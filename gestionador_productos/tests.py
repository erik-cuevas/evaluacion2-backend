"""Tests básicos para validar modelo y vista de listado."""

from django.test import TestCase
from django.urls import reverse
from .models import Producto


class ProductoModelTest(TestCase):
    """Prueba simple para verificar creación de Producto."""

    def test_crear_producto(self):
        p = Producto.objects.create(nombre="Test", descripcion="desc", precio=9.99)
        self.assertEqual(str(p).startswith("Test"), True)


class ProductoListViewTest(TestCase):
    """Comprueba que la vista de listado responde y contiene el texto esperado."""

    def setUp(self):
        Producto.objects.create(nombre="P1", descripcion="d1", precio=1.0)
        Producto.objects.create(nombre="P2", descripcion="d2", precio=2.0)

    def test_listado_status_code(self):
        url = reverse('listado')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Listado de Productos")

    # Nota: estos tests usan la base de datos de pruebas proporcionada por
    # Django (se crea y destruye automáticamente). No tocan archivos en
    # MEDIA_ROOT. Para pruebas de subida de archivos se recomienda usar
    # django.core.files.uploadedfile.SimpleUploadedFile.
