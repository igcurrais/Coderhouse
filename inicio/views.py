from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Bebida

def inicio(request):
    # return HttpResponse('<h1>ESTE ES MI PRIMERA VISTA</h1>')
    return render(request, 'inicio.html')

def crear_bebida(request):
    return render(request, "crear_bebida.html")
