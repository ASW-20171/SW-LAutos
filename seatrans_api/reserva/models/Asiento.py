from django.db import models


class Asiento(models.Model):

    tipo_asiento = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=50)
    costo = models.FloatField()

    class Meta:
        verbose_name = "Asiento"
        verbose_name_plural = "Asientos"

    def __str__(self):
        return self.tipo_asiento
