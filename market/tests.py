from django.test import TestCase
from django.urls import reverse
from .models import Producto


class ProductoModelTest(TestCase):
	def test_crear_producto(self):
		p = Producto.objects.create(nombre="Test", descripcion="desc", precio=9.99)
		self.assertEqual(str(p).startswith("Test"), True)


class ProductoListViewTest(TestCase):
	def setUp(self):
		Producto.objects.create(nombre="P1", descripcion="d1", precio=1.0)
		Producto.objects.create(nombre="P2", descripcion="d2", precio=2.0)

	def test_listado_status_code(self):
		url = reverse('listado')
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, "Listado de Productos")
