from django.db import models
from .Cliente import Cliente
from .Asiento import Asiento

# Create your models here.


class Reserva(models.Model):

    descripcion = models.CharField(max_length=60)
    estado = models.BooleanField(default=True)
    fecha_reserva = models.DateTimeField(auto_now_add=True, null=True)
    costo = models.FloatField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    asiento = models.ForeignKey(Asiento, null=True, blank=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return '%s %s' % (self.descripcion, self.horario.origen)
