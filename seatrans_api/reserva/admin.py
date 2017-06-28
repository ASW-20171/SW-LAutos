from django.contrib import admin
from .models.Reserva import Reserva
from .models.Origen import Origen
from .models.Destino import Destino
from .models.Cliente import Cliente
from .models.Asiento import Asiento
from .models.Horario import Horario
from .models.Pago import Pago
# Register your models here.


class HorarioAdmin(admin.ModelAdmin):
    """docstring for HorarioAdmin"""
    list_display = ("fecha_salida", "hora_salida", "origen", "destino")
    search_fields = ("fecha_salida", "hora_salida")
    list_per_page = 3

admin.site.register(Horario, HorarioAdmin)
admin.site.register(Origen)
admin.site.register(Destino)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Cliente)
admin.site.register(Asiento)
