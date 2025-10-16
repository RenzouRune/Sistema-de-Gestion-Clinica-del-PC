from django.db import models

# Create your models here.

class usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)    
    rol = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class roles(models.Model):
    nombre_rol = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_rol