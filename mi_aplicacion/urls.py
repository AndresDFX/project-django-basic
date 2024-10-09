from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('saludo/', views.saludos),
    path('saludo-post/', views.saludo_post),
    path('saludo-vista-clase', views.SaludoView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/saludo-rest/', views.SaludoViewAPI.as_view(), name="saludo")
]


