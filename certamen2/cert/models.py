from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proyecto_propuesto", null=True)
    patrocinado = models.BooleanField(default=False)
    profesor_patrocinador = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="proyecto_patrocinado")

    def __str__(self) -> str:
        return self.nombre

    
