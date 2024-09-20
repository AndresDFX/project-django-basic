from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludos),
    path('saludo-post/', views.saludo_post),
    path('saludo-vista-clase', views.SaludoView.as_view())
]


