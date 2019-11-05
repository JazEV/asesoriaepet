from django.contrib import admin
from .models import Turno, Horario, Novedad

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):

	list_filter = ('nombre', 'apellido')
	search_fields = ['nombre__icontains', 'apellido']
	list_display = ('nombre', 'apellido')

from .models import Turno

@admin.register(Horario)
class TurnoAdmin(admin.ModelAdmin):
	fieldsets = [
        (None, {'fields': ['nombre', 'apellido']}),
        ('Lunes:', {'fields': ['hora_1_inicio', 'hora_1_fin']}),
        ('Martes:', {'fields': ['hora_2_inicio', 'hora_2_fin']}),
        ('Miercoles:', {'fields': ['hora_3_inicio', 'hora_3_fin']}),
        ('Jueves:', {'fields': ['hora_4_inicio', 'hora_4_fin']}),
        ('Viernes:', {'fields': ['hora_5_inicio', 'hora_5_fin']}),
    ]
	list_filter = ('nombre', 'apellido')
	search_fields = ['nombre__icontains']

@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	model = Novedad
	list_filter = ['titulo']
	search_fields = ['titulo']
