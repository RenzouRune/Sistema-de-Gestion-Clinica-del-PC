from django.db import models

# Create your models here.

class roles(models.Model):
    nombre_rol = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_rol

class usuarios(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.ForeignKey(roles, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.nombre
