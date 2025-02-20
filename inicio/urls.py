from django.urls import path
from inicio.views import inicio, crear_bebida, listar_bebidas

urlpatterns = [
    path("",inicio,name="inicio"),
    path("crear_bebida/", crear_bebida,name="crear_bebida"),
    path('listar_bebidas/',listar_bebidas ,name="listar_bebidas")
]