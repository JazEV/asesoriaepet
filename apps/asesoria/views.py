from rest_framework import viewsets
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Turno, Horario, Novedad,
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS
from .serializers import TurnoSerializer, HorarioSerializer, NovedadSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

class TurnoViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

class TurnoCreate(CreateView):
	model = Turno
	fields = ['nombre', 'apellido', 'horario', 'motivo', 'telefono', 'email', 'nota']
	template_name = 'turno/index.html'
	success_url = reverse_lazy('turno:turno_create')

class HorarioViewSet(viewsets.ModelViewSet):
	queryset = Turno.objects.all()
	serializer_class = TurnoSerializer

class NovedadViewSet(viewsets.ModelViewSet):
	queryset = Novedad.objects.all()
	serializer_class = NovedadSerializer

class IndexView(LoginRequiredMixin, ListView):
	model = Novedad
	template_name = 'index.html'
	context_object_name = 'novedades'

class NovedadDetail(LoginRequiredMixin, DetailView):
	model = Novedad
	template_name = 'novedad/detalle.html'
	context_object_name = 'novedad'


# Sirve para crear un formulario y dar de alta una Novedad fuera del admin
class NovedadCreate(LoginRequiredMixin, CreateView):
	model = Novedad
	fields = ['titulo']
	template_name = 'novedad/create.html'
	success_url = reverse_lazy('novedades:index')


class NovedadUpdate(LoginRequiredMixin, UpdateView):
	model = Novedad
	fields = ['titulo']
	template_name = 'novedad/update.html'
	success_url = reverse_lazy('novedades:index')


class NovedadDelete(LoginRequiredMixin, DeleteView):
	model = Novedad
	template_name = 'novedad/delete.html'
	success_url = reverse_lazy('novedades:index')
