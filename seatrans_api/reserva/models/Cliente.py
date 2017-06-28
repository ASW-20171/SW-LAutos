from django.db import models
from .Reserva import Reserva


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=20, null=False, blank=False)
    apellidos = models.CharField(max_length=60, null=False)
    celular = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=50, null=False)
    reserva = models.ForeignKey(Reserva, null=True, blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
