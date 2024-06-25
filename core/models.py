from django.db import models

# Create your models here.
tipo_entrada = [
    ("0" , "entrada"),
    ("1" , "salida")
]

tipo_vehiculo = [
    ("M" , "moto"),
    ("A" , "Auto")
]

class Acceso(models.Model):
    fecha = models.DateTimeField()
    acceso = models.CharField(max_length=20, choices=tipo_entrada)
    vehiculo = models.CharField(max_length=10, choices=tipo_vehiculo)


class Estacionamiento(models.Model):
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=20)
    ocupado = models.BooleanField(default=False)
