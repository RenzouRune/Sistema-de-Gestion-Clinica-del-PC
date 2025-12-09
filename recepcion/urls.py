from django.urls import path
from . import views
from .api_views import api_lista_equipos, api_registrar_equipo, api_modificar_equipo, api_eliminar_equipo

urlpatterns = [
    path('recepcion/', views.recepcion_view, name='recepcion'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<str:nombre>/', views.detalle_equipo, name='detalle_equipo'),
    path('editar_equipo/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('delete_equipo/<int:id>/', views.delete_equipo, name='delete_equipo'),
    path('api/recepcion/', api_lista_equipos, name='api_lista_cultivos'),
    path('api/recepcion/registrar/', api_registrar_equipo, name='api_registrar_equipo'),
    path('api/recepcion/modificar/<int:pk>/', api_modificar_equipo, name='api_modificar_equipo'),
    path('api/recepcion/eliminar/<int:pk>/', api_eliminar_equipo, name='api_eliminar_equipo'),
]
