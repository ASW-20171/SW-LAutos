from django.db import models

# Create your models here.


class Reserva(models.Model):

    descripcion = models.CharField(max_length=60)
    codigo = models.CharField(max_length=60, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_reserva = models.DateField()

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __str__(self):
        return self.descripcion
