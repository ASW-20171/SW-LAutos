from django.db import models
from .Horario import Horario
from .Asiento import Asiento

# Create your models here.


class Reserva(models.Model):

    descripcion = models.CharField(max_length=60)
    codigo = models.CharField(max_length=60, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_reserva = models.DateField(null=True, blank=True)
    costo = models.FloatField(null=True, blank=True)
    horario = models.ForeignKey(Horario, null=True, blank=True)
    asiento = models.ForeignKey(Asiento, null=True, blank=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.descripcion
