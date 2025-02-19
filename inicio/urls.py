from django.urls import path
from inicio.views import inicio, crear_bebida

urlpatterns = [
    path("",inicio,name="inicio"),
    path("crear_bebida/", crear_bebida,name="crear_bebida")
]