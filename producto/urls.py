from django.urls import path
from . import views

urlpatterns = [
    path('lista-productos/', views.lista_productos, name="producto_lista"),
    path('<int:pk>/', views.ProductoDetalleView.as_view(), name='producto_detalle'),
]


