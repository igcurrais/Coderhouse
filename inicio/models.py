from django.db import models

# Create your models here.
class Bebida(models.Model):
    tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.tipo} {self.nombre}'