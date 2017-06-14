from django.db import models


class Cliente(models.Model):

    nombres = models.CharField(max_length=60)
    codigo = models.CharField(max_length=20, null=False, blank=False)
    apellidoP = models.CharField(max_length=60, null=False)
    apellidoM = models.CharField(max_length=60, nul=False)
    direccion = models.CharField(max_length=60, null=True)
    celular = models.CharField(max_length=60, null=True)
    email = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombres
