from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import permission_required
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer
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




class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoListCreate2(APIView):

    def get(self, request):
        # AGREGAR AL PRIMER ELEMENTO DE LA RESPUESTA LA CLAVE "test: 1"
        #productos = Producto.objects.filter(descripcion="a")
        productos = list(Producto.objects.all())
        productos[0].test = 1
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)


        # Actualizar el producto
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





