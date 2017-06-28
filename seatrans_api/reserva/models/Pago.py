from django.db import models


class Pago(models.Model):

    detalle_pago = models.CharField(max_length=60)
    codigo = models.CharField(max_length=50, null=False)
    monto = models.FloatField(null=True, blank=True)
    sub_total = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return self.detalle_pago
