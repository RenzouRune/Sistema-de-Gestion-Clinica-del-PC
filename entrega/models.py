from django.db import models
from diagnostico.models import Diagnostico

# Create your models here.

class Reporte(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Entregado', 'Entregado'),
    ]
    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reporte de {self.diagnostico.asignacion} - {self.estado}"
