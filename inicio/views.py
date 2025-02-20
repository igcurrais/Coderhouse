from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Bebida
from inicio.forms import CrearBebida


def inicio(request):
    # return HttpResponse('<h1>ESTE ES MI PRIMERA VISTA</h1>')
    return render(request, 'inicio.html')

def crear_bebida(request):
    formulario = CrearBebida()
    if request.method == "POST":
        formulario = CrearBebida(request.POST)
        if formulario.is_valid():
            formulario.cleaned_data
            bebida = Bebida(tipo=formulario.cleaned_data.get('tipo'),
                            nombre=formulario.cleaned_data.get('nombre'),
                            descripcion=formulario.cleaned_data.get('descripcion')
                            )
            bebida.save()   
        
    return render(request, 'crear_bebida.html', {'formulario': formulario})

def listar_bebidas(request):
    bebidas = Bebida.objects.all()
    return render(request, 'listar_bebidas.html',{'bebidas':bebidas})