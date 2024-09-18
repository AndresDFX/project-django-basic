import random

from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        aleatorio = random.randint(1, 6)
        return f"{self.titulo}{aleatorio}"

