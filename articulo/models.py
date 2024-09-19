import random

from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1)

    def __str__(self):
        aleatorio = random.randint(1, 6)
        return f"{self.titulo}{aleatorio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now_add=True)


