from django.contrib import admin
from .models import Reserva
# Register your models here.


class ReservaAdmin(admin.ModelAdmin):
    """docstring for ReservaAdmin"""
    list_display = ("descripcion", "codigo", "estado")
    search_fields = ("descripcion", "codigo")
    list_per_page = 3

admin.site.register(Reserva, ReservaAdmin)
