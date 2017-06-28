from django.db import models


class Origen(models.Model):

    nombre_origen = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Origen"
        verbose_name_plural = "Origens"

    def __str__(self):
        return self.nombre_origen
