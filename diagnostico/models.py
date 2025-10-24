from django.db import models
from recepcion.models import Equipo

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipo} asignado a {self.estudiante}"

class Diagnostico(models.Model):
    asignacion = models.OneToOneField(Asignacion, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    solucion = models.TextField()

    def __str__(self):
        return f"Diagnóstico de {self.asignacion}"
