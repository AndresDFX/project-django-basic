from django.db import models

from articulo.models import Cliente
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    nombre_pedido = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)


