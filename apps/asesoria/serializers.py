from rest_framework import serializers
from .models import Turno, Novedad, Horario

class TurnoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Turno
		fields = ['nombre', 'apellido', 'horario', 'nota']

class HorarioSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Turno
		fields = ('nombre', 'apellido', 'hora_1_inicio', 'hora_1_fin',
		'hora_2_inicio', 'hora_2_fin', 'hora_3_inicio', 'hora_3_fin',
		'hora_4_inicio', 'hora_4_fin', 'hora_5_inicio', 'hora_5_fin')

class NovedadSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Novedad 
		fields = ('titulo', 'texto', 'imagen')
