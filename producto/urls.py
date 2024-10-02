from django.urls import path
from . import views
from .views import ProductoListCreate, ProductoListCreate2

urlpatterns = [
    path('crear-producto/', views.crear_producto, name="crear_producto"),
    path('lista-productos/', views.lista_productos, name="producto_lista"),
    path('<int:pk>/', views.ProductoDetalleView.as_view(), name='producto_detalle'),
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos2/', ProductoListCreate2.as_view(), name='producto-list-create2'),
    path('api/productos2/<int:pk>', ProductoListCreate2.as_view(), name='producto-list-create2'),
]


