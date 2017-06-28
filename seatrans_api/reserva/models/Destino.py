from django.db import models


class Destino(models.Model):

    nombre_destino = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"

    def __str__(self):
        return self.nombre_destino
