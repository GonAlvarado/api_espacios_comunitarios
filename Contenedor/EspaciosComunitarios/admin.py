from django.contrib import admin
from .models import ReferenteDb, EspacioDb, RetiroDb, DiaDb, HorarioDb

admin.site.site_header = "Dirección de Desarrollo Social Berisso"
admin.site.index_title = "Registro de Espacios Comunitarios"
admin.site.site_title = "Dirección de Desarrollo Social Berisso"

class DiaAdmin(admin.ModelAdmin):
    fields = ["dia"]
    list_display = ["dia"]

admin.site.register(DiaDb, DiaAdmin)

class HorarioAdmin(admin.ModelAdmin):
    fields = ["horario"]
    list_display = ["horario"]

admin.site.register(HorarioDb, HorarioAdmin)

class ReferenteAdmin(admin.ModelAdmin):
    fields = ["nombre", "apellido", "telefono", "dni"]
    list_display = ["nombre", "apellido", "telefono", "dni"]

admin.site.register(ReferenteDb, ReferenteAdmin)

class EspacioAdmin(admin.ModelAdmin):
    fields = ["tipo", "nombre", "direccion", "coordenadas", "dia", "horario", "barrio", "tarjeta", "asistencia", "referente_fk"]
    list_display = ["tipo", "nombre", "direccion", "barrio", "tarjeta", "asistencia", "referente_fk"]
    search_fields = ["nombre"]
    list_filter = ["dia", "horario"]

admin.site.register(EspacioDb, EspacioAdmin)

class RetiroAdmin(admin.ModelAdmin):
    fields = ["fecha", "descripcion", "agente", "espacio_fk"]
    list_display = ["fecha", "descripcion", "agente", "espacio_fk"]

admin.site.register(RetiroDb, RetiroAdmin)