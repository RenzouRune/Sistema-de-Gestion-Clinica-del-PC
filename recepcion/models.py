from django.db import models

# Create your models here.

class Equipo(models.Model):
    cliente = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    problema = models.TextField()
    fecha_recepcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.cliente}"
