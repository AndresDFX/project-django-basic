from django.shortcuts import render

from .models import Articulo


def lista_articulos(request):
    articulos = Articulo.objects.all()  #Consulta a la base de datos trayendo todos los objetos
    return render(request, 'lista_articulos.html', {'articulos': articulos})
