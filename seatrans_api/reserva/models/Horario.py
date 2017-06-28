from django.db import models
from .Origen import Origen
from .Destino import Destino


class Horario(models.Model):

    fecha_salida = models.DateField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    descripcion_horario = models.CharField(max_length=20, blank=True)
    origen = models.ForeignKey(Origen, null=True, blank=True)
    destino = models.ForeignKey(Destino, null=True, blank=True)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    def __str__(self):
        return self.descripcion_horario
