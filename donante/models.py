from django.db import models


class DonanteModel(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
