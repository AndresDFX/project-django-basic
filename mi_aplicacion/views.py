from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def saludos(a):
    print(a) #imprime un objeto
    return HttpResponse("¡Hola, Django! Get")


def saludo_post(a):
    print(a) #imprime un objeto
    return HttpResponse("¡Hola, Django! Post")

class SaludoView(View):
    def get(self, request):
        return HttpResponse("¡Hola desde una vista basada en clase!")

    def post(self, request):
        ...