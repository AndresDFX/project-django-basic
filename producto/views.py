from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import permission_required

from .permissions import group_required


@group_required('admin')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productoss': productos})



class ProductoDetalleView(DetailView):
    model = Producto
    template_name = 'producto_detalle.html'



#@login_required
@permission_required('producto.add_producto', '/login/')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})
