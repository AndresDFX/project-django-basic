from django.shortcuts import render
from django.views.generic import DetailView
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productoss': productos})



class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'
