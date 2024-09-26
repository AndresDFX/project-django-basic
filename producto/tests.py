from django.test import TestCase
from django.urls import reverse

from .models import Producto
class ProductoTestCase(TestCase):
    def setUp(self): #Definir que necesito para mi prueba o conjunto de pruebas
        Producto.objects.create(nombre="Producto 1", precio=100)

    def test_producto_nombre(self):
        producto = Producto.objects.get(nombre="Producto 1") #Trayendo el objecto producto
        self.assertEqual(producto.nombre, "Producto 1")


class CrearProductoViewTest(TestCase):

    def test_post_crear_producto_valido(self):
        data = {
            "nombre": "Producto2",
            "precio": "10.99"

        }
        self.client.post(reverse("crear_producto"), data)
        self.assertEqual(Producto.objects.count(), 1)

