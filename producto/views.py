from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Producto
from .forms import ProductoForm


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productoss': productos})



class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'




def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})
