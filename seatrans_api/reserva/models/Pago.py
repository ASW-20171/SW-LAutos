from django.db import models
from .Cliente import Cliente
from .Reserva import Reserva


class Pago(models.Model):

    detalle_pago = models.CharField(max_length=60)
    monto = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)
    reserva = models.ForeignKey(Reserva, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return self.detalle_pago
