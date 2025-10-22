from django.db import models
from diagnostico.models import Asignacion

# Create your models here.

class Entrega(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Entregado', 'Entregado'),
    ]
    asignacion = models.OneToOneField(Asignacion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega de {self.asignacion} - {self.estado}"
