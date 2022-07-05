import email
from django.db import models

# Create your models here.
class InformeSemanalModel(models.Model):
    email = models.EmailField(max_length=100, null=False)
    fecha = models.DateTimeField(auto_now_add=True)


class EncuestaModel(models.Model):
    pregunta = models.CharField(max_length=100, default='¿Cual es tu club favorito?')
    respuesta = models.TextField(null= False)
    fecha = models.DateTimeField(auto_now_add=True)

class ContactenosModel(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=150, null=False)
    asunto = models.CharField(max_length=200, null=False)
    mensaje = models.TextField(null=False)
    fecha = models.DateTimeField(auto_now_add=True)

class EquiposModel(models.Model):
    def __str__(self):
        return f"Equipo: {self.equipo}"
    equipo = models.CharField(max_length=150, null=False)
    fundacion = models.IntegerField(null=False)
    presidente = models.CharField(max_length=150, null=False)
    dt = models.CharField(max_length=150, null=False)
    division = models.CharField(max_length=150, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
