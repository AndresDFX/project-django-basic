from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Producto
from user_custom.models import CustomUser


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



class ProductoListaCreateView(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test_user@admin.com", password="test_user")
        self.token = Token.objects.create(user=self.user)
        self.producto1 = Producto.objects.create(nombre="Producto1", descripcion="P", precio=10.15)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTORIZATION=f'Token {self.token.key}')
        self.url = "/producto/api/productos2/"

    def test_get_productos(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)


