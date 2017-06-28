from django.db import models


class Cliente(models.Model):

    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60, null=False)
    email = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
