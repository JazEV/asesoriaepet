from django.urls import include, path 
from rest_framework import viewsets
from rest_framework import routers 
from .views import (TurnoViewSet, TurnoCreate, HorarioViewSet,
NovedadViewSet, IndexView, NovedadDetail, 
NovedadCreate, NovedadUpdate, NovedadDelete
)

router = routers.DefaultRouter()
router.register('novedades', NovedadViewSet)
router.register('turno', TurnoViewSet)
router.register('horario', HorarioViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('', IndexView.as_view(), name="index"),
	path(
    	route='detalle/<int:pk>',
    	view=NovedadDetail.as_view(),
    	name='detalle'
    ),
    path(
    	route='novedad/create/',
    	view=NovedadCreate.as_view(),
    	name='novedad_create'
    ),
    path(
    	route='novedad/update/<int:pk>',
    	view=NovedadUpdate.as_view(),
    	name='novedad_update'
    ),
    path(
    	route='novedad/delete/<int:pk>',
    	view=NovedadDelete.as_view(),
    	name='novedad_delete'
    ),
	path(
    	route='turno',
    	view=TurnoCreate.as_view(),
    	name='turno_create'
    ),
]
