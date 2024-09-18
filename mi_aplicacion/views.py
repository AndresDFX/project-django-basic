from django.shortcuts import render
from django.http import HttpResponse

def saludos(a):
    print(a) #imprime un objeto
    return HttpResponse("¡Hola, Django!")

